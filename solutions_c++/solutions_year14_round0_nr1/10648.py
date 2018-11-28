#include<cstdio>
#include<algorithm>
#include<iostream>
#include<set>
#include<map>

using namespace std;

int tc,m,n,p,nos;
int main()
{
	nos =1 ;
	scanf("%d",&tc);
	while( tc-- )
	{
		set<int> S;
		map<int,int> M;
		scanf("%d",&m);m--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&p);
				if( m == i ) { S.insert(p); M[p] = M[p]+1;}
			}
		}
		scanf("%d",&n);n--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&p);
				if( n == i ) { S.insert(p); M[p] = M[p] + 1;}
			}
		}

		if( (int)S.size() == 7 ) 
		{
			int ans = 0;
			for(map<int,int>::iterator it = M.begin() ; it != M.end() ; it++ )
			{
				if( it->second == 2 )
				{
					ans = it->first;
					break;
				}
			}
			printf("Case #%d: %d\n",nos,ans);
		}
		else if( (int)S.size() < 7 ) printf("Case #%d: Bad magician!\n",nos);
		else if( (int)S.size() >= 8  ) printf("Case #%d: Volunteer cheated!\n",nos);
		nos++;
	}
	return 0;
}
