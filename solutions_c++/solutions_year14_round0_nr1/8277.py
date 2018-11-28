#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<bitset>
#include<map>
#include<utility>
#include<string>
#include<cstring>
#include<queue>
#include<sstream>

using namespace std ;

int grid1[5][5] ;
int grid2[5][5] ;
vector<int> list ;

int main ()
{
	freopen ("test.txt","w",stdout);

	int t , r1,r2 , c =0 ;

	cin>>t;

	while(t--)
	{
		list.clear() ;
		c++;
		cin>>r1 ;
		r1-- ;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>grid1[i][j];

		cin>>r2 ;
		r2--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>grid2[i][j] ;

		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(grid1[r1][i] == grid2[r2][j])
					list.push_back(grid1[r1][i]);

		if(list.size()==0)
			printf("Case #%d: Volunteer cheated!\n",c);
		else
			if(list.size()==1)
				printf("Case #%d: %d\n",c,list[0]);
			else
				printf("Case #%d: Bad magician!\n",c);
	}

	return 0;
}
