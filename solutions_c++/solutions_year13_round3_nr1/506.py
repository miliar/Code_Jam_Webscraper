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

char s[1000005];
int N;

bool vowel(char x)
{
	return x=='a' || x=='e' || x=='i' || x=='u' || x=='o';
}

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("A.out","w",stdout);
	
	int T,k=0;
	
	scanf("%d",&T);
	
	while(T--)
	{
		k++;
		
		scanf("%s %d",s,&N);
		
		int M=strlen(s);
		int last=-1;
		int c=0;
		LL ret=0;
		
		fo(i,M)
		{
			if(!vowel(s[i]))
				c++;
			else c=0;
			
			if(c>=N)last=i-N+1;
			
			if(last!=-1)
				ret+=last+1;
		}
		
		printf("Case #%d: %lld\n",k,ret);
	}
}


































