#include <bits/stdc++.h>
#define sflld(n) scanf("%lld",&n)
#define sfulld(n) scanf("%llu",&n)
#define sfd(n) scanf("%d",&n)
#define sfld(n) scanf("%ld",&n)
#define sfs(n) scanf("%s",&n)
#define ll long long
#define s(t) int t; while(t--)
#define ull unsigned long long int
#define pflld(n) printf("%lld\n",n)
#define pfd(n) printf("%d\n",n)
#define pfld(n) printf("%ld\n",n)
#define lt 2*idx
#define rt 2*idx+1
#define f(i,k,n) for(i=k;i<n;i++)
#define MAXN 0

using namespace std;

int main()
{
    int t,tc=1,i;
	sfd(t);
	while(t--)
    {
		string s;
		cin>>s;
		int l=s.length();
        int ct=1;
		f(i,1,l)
		{
			if(s[i]!=s[i-1])
                ct++;
		}
        if(s[l-1]=='+')
            ct--;
		printf("Case #%d: %d\n",tc++,ct);
	}
	return 0;
}
