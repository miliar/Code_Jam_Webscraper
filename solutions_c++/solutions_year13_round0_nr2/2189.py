#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;


int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,n,m;
	cin>>T;
	for (int z = 0; z < T; z++)
	{
		cin>>n>>m;
		vector<vector<int> >v(n,vector<int>(m,0));
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				cin>>v[i][j];
			}
		}
		bool WRONG = false;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				bool WRONGA = false,WRONGB = false;
				for (int x = 0; x < m; x++)
				{
					if(v[i][x]>v[i][j]){WRONGA=true;}
				}
				for (int x = 0; x < n; x++)
				{
					if(v[x][j]>v[i][j]){WRONGB=true;}
				}
				WRONG=WRONGA&&WRONGB;
				if(WRONG)break;
			}
			if(WRONG)break;
		}
		if(!WRONG)printf("Case #%d: YES\n",z+1);
		else printf("Case #%d: NO\n",z+1);
	}

}