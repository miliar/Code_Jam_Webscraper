//@author:ReVo
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <map>
#include <algorithm>
#include <stack>
#include <list>

//Shortcuts
#define lli long long int
#define fo(i,n) for(i=0;i<n;i++)
#define fi(i,a,n) for(i=a;i<=n;i++)
#define fd(i,n,a) for(i=n;i>=a;i--)
#define modulo 1000000007
#define gi(a) scanf("%d",&a)
#define f(n) for(i=0;i<n;i++)
#define pn printf("\n")
#define pb push_back

using namespace std;

int main()
{
	int t,case_number=1;
	int ans,aud,k,smax;
	cin>>t;
	while(t--)
	{
		ans=aud=0;
		cin>>smax;
		char s[1001];
		scanf("%s",s);
		fi(k,0,smax+1)
		{
			if(s[k]!='0')
			{
				if(aud>=k)
					aud+=s[k]-'0';
				else
				{
					ans+=(k-aud);
					aud+=((k-aud)+(s[k]-'0'));
				}
			}
		}
		printf("Case #%d: %d\n",case_number,ans);
		case_number++;
	}
    return 0;
}
