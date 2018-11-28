#include<cstdio>
#include<iostream>
#include<cassert>
#include<cctype>
#include<cfloat>
#include<climits>
#include<cstring>
#include<bitset>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<vector>
#include<algorithm>
#include<string>
#include<climits>
#include<cmath>
using namespace std;
int main()
{
	int ar[5][5],br[5][5],a,b,i,j,t,f,k=0,l;
	scanf("%d",&t);
	while(t--)
	{
		k++;
		f=0;
		scanf("%d",&a);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&ar[i][j]);
		scanf("%d",&b);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&br[i][j]);
		a--;
		b--;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				//cout<<ar[a][i]<<" "<<br[b][j]<<endl;
				if(ar[a][i]==br[b][j])
				{
					l=ar[a][i];
					f++;
				}
			}
			//cout<<"-----"<<endl;
		}
		//cout<<a<<" "<<b<<" "<<f<<endl;
		if(f==1)
			printf("Case #%d: %d\n",k,l);
		else if(f>1)
			printf("Case #%d: Bad magician!\n",k);
		else
			printf("Case #%d: Volunteer cheated!\n",k);
	}

	return 0;
}

