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

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("output.out","w",stdout);
    
    int T,k=0;
    scanf("%d",&T);
    
    while(T--)
    {
		k++;
		printf("Case #%d: ",k);
		
		LL N,M;
		int ret=0;
		
		scanf("%lld/%lld",&N,&M);
		
		while(N<M)
		{
			N*=2;
			ret++;
		}
		long long diff = N-M, gen=ret;
		while(diff && gen<=40)
		{
			while(diff<M)
			{
				diff*=2;
				gen++;
			}
			
			diff = diff - M;
		}
		if(gen>40)printf("impossible\n");
		else printf("%d\n",ret);
	}
}


































