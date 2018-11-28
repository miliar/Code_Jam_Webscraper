#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<sstream>
#include<iostream>
#include<stack>
#include<list>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)
#define MOD  1000000007

int maznoo2[55],yebda2[55],yentehy[55],all[55],yebda2_ind[55];
bool ifall[105];
bool vis[105],FLAG;
int comp;
vs s;

bool checkValidity(vs s)
{
	fo(i,(int)s.sz)
	{
		int segments=0,cnt=1;
		s[i]+='#';
		for(int j=1;j<(int)s[i].sz;j++)
		{
			if(s[i][j] != s[i][j-1])
			{
				if(s[i][j] == '#')
				{
					if(segments == 0)
					{
						all[s[i][j-1]-'a'] ++;
						ifall[i] = 1;
					}
					else
					{
						yentehy[s[i][j-1]-'a'] ++;
					}
				}
				else
				{
					if(segments == 0)
					{
						yebda2[s[i][j-1]-'a'] ++;
						yebda2_ind[s[i][j-1]-'a'] = i;
					}
					else
					{
						maznoo2[s[i][j-1]-'a'] ++;
					}
				}
				cnt = 1;
				segments++;
			}
			else cnt++;
		}
	}
	
	for(int i=0;i<26;i++)
	{
		if(maznoo2[i] > 1 || yebda2[i] > 1 || yentehy[i] > 1)return 0;
		if(maznoo2[i] && (yebda2[i] || yentehy[i] || all[i]))return 0;
	}
	return 1;
}

void flood(int ind)
{
	if(ind == -1)return;
	if(vis[ind])
	{
		if(vis[ind] < comp)
			comp--;
		else if(vis[ind] == comp)
			FLAG = 1;
		return;
	}
	
	vis[ind] = 1;
	
	int L = s[ind].size();
	
	//printf("%d ** \n",yebda2_ind[s[ind][L-1]-'a']);
	
	flood(yebda2_ind[s[ind][L-1]-'a']);
}


long long fact[107];

int main()
{
    freopen ("B-small-attempt1.in","r",stdin);
    freopen ("output.out","w",stdout);
    
    int T,k=0;
    scanf("%d",&T);
    
    fact[0]=1;
    for(int i=1;i<=105;i++)
    {
		fact[i] = fact[i-1]*i;
		fact[i] %= MOD;
	}
    
    while(T--)
    {
		FLAG = 0;
		clr(vis,0);
		comp = 0;
		s.clear();
		clr(ifall,0);
		clr(yebda2,0);
		clr(yebda2_ind,-1);
		clr(yentehy,0);
		clr(maznoo2,0);
		clr(all,0);
		
		k++;
		printf("Case #%d: ",k);
		
		int N;
		
		scanf("%d",&N);
		
		fo(i,N)
		{
			char cc[105];
			scanf("%s",cc);
			s.push_back(string(cc));
		}
		
		if(!checkValidity(s))
		{
			printf("0\n");
			continue;
		}
		
		for(int i=0;i<N;i++)
		{
			if(!ifall[i])
			{
				if(!vis[i])
				{
					comp++;
					flood(i);
				}
			}
		}
		for(int i=0;i<26;i++)
		{
			if(all[i] && !yebda2[i] && !yentehy[i])
			{
				comp ++;
			}
		}
		
		long long ret = fact[comp];
		
		for(int i=0;i<26;i++)
		{
			ret *= fact[all[i]];
			ret %= MOD;
		}
		if(FLAG)printf("0\n");
		else printf("%d\n",(int)ret);
	}
}


/*
1
3
a b b

*/



























