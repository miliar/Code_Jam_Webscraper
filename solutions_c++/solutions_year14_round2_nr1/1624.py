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

char s[105][105];
int N,best[105];
vector<int> C[105];

string get(string S)
{
	string ret;
	S+='#';
	fo(i,(int)S.sz-1)
	{
		if(S[i] != S[i+1])
			ret+=S[i];
	}
	return ret;
}

void cat()
{
	
	fo(i,N)
	{
		C[i].clear();
		int cnt=1;
		string S=s[i];
		S+='#';
		fo(j,(int)S.sz-1)
		{
			if(S[j] != S[j+1])
			{
				C[i].pb(cnt);
				cnt=1;
				continue;
			}
			
			cnt++;
		}
	}
}

int solve(int ind)
{
	if(ind == (int)C[0].size())return 0;
	
	if(best[ind]!=-1)return best[ind];
	
	int ret=1<<28;
	for(int i=0;i<=100;i++)
	{
		int sum=0;
		fo(j,N)
			sum+=abs(C[j][ind] - i);
		ret=min(ret,sum+solve(ind+1));
	}
	return best[ind]=ret;
}

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("output.out","w",stdout);
    
    int T,k=0;
    scanf("%d",&T);
    
    while(T--)
    {
		int ret=1<<30;
		bool f=0;
		
		k++;
		printf("Case #%d: ",k);
		
		scanf("%d",&N);
		fo(i,N)
			scanf("%s",s[i]);
		
		string base = get(s[0]);
		
		for(int i=1;i<N;i++)
		{
			if(get(s[i]) != base)
			{
				printf("Fegla Won\n");
				f=1;
				break;
			}
		}
		if(f)continue;
		
		cat();
		
		clr(best,-1);
		ret=solve(0);
		
		printf("%d\n",ret);
	}
}


































