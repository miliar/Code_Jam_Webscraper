#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define pb push_back

using namespace std;

const int MAXN = 110;
const int INF  = 1000000010;
const int mod  = 1000003;

typedef long long Lint;
typedef pair <int,int> pii;

int n,m,r;
int ar[MAXN];
char Map[MAXN][MAXN];
bool banned[MAXN][MAXN][128];
int main()
{
	int Test , tt;
	scanf(" %d",&Test);
	for(tt=1;tt<=Test;tt++){
		printf("Case #%d: ",tt );
		memset(banned,0,sizeof(banned));
		scanf(" %d %d",&n,&m);
		for(int i = 0 ; i < n ; i++)
			for(int j = 0 ; j < m ;j++)
				scanf(" %c",&Map[i][j]);
		int res = 0;
		for(int i = 0 ; i < n ; i++)
		{
			for(int j = 0 ; j < m ; j++){
				if(Map[i][j] != '.')
				{
					banned[i][j]['<'] = 1;
					break;
				}
			}
			for(int j = m-1 ; j >= 0 ; j--){
				if(Map[i][j] != '.')
				{
					banned[i][j]['>'] = 1;
					break;
				}
			}
		}
		for(int j = 0 ; j < m ; j++)
		{
			for(int i = 0 ;i < n ; i++){
				if(Map[i][j] != '.')
				{
					banned[i][j]['^'] = 1;
					break;
				}
			}
			for(int i = n-1 ; i>=0; i--){
				if(Map[i][j] != '.')
				{
					banned[i][j]['v'] = 1;
					break; 
				}
			}
		}
		bool impossible = false;
		for(int i = 0; i < n ;i++)
			for(int j = 0 ;j < m; j++){
				if(Map[i][j]!='.'){
					if(banned[i][j][Map[i][j]]){
						res++;
						if(banned[i][j]['v'])
							if(banned[i][j]['>'])
								if(banned[i][j]['<'])
									if(banned[i][j]['^'])
										impossible = true;
					}
				}
			}
		if(impossible) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
	return 0;
}
