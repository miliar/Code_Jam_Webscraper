#include<bits/stdc++.h>
using namespace std;
#define fast cin.sync_with_stdio(0);cin.tie(0)
#define pii pair<int,int>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define INF 99999999
#define N 100005
#define ll long long
#define llu unsigned long long 
#define MOD 1000000007
#define gcd __gcd
#define fill(A,v) memset(A,v,sizeof(A))
int main()
{
	int t,k,i;
	scanf("%d",&t);
    for(k=1;k<=t;k++)
	{
		char s[N],str[N];
		deque<char> dq;
		char c;
		int len=0;
		scanf("%s",s);
		int l=strlen(s);
		dq.push_back(s[0]);
		for(i=1;i<l;i++)
		{
			c=dq.front();
			if(s[i]>=c)
			  dq.push_front(s[i]);
			else
			  dq.push_back(s[i]);
	    }
	    while(!dq.empty())
	    {
	    	c=dq.front();
	    	str[len++]=c;
	    	dq.pop_front();
	    }
		str[len]='\0';
		printf("Case #%d: %s\n",k,str);
	}
	return 0;
}	