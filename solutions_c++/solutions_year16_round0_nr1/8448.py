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
int sol(int n){
	if(n==0)
		return -1;

	int m=0;
	int r=(1<<10)-1;
	int ct = 1;
	while(m!=r)
    {
		int num=ct*n;
		while(num>0)
		{
			int r = num%10;
			m|=(1<<r);
			num/= 10;

		}
        ct++;
	}
	return --ct*n;
}
int main(){
	int t,tc=1;
	sfd(t);
	while(t--)
    {
		int n;
		sfd(n);
		printf("Case #%d: ", tc++);
		int ans = sol(n);
		if(ans == -1)
        {
			printf("INSOMNIA\n");
		}
        else
        {
			pfd(ans);
		}
	}

	return 0;
}
