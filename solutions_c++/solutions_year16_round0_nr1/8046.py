#include <algorithm>
#include <cstring>
#include <cmath>
#include <set>
#include <vector>
#include <cstdio>
#include <iostream>
#define S(x) scanf("%lld",&x)
#define P(x) printf("%lld",x)
#define LI long long int
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		LI n,a[10],cover=0,temp,ans;
		S(n);
		for(int i=0;i<10;i++) a[i]=0;
		for(int i=1;i<1000000;i++)
		{
			temp=i*n;
			while(temp>0)
			{
				if(a[temp%10]==0)
				{
					 a[temp%10]=1;
					 cover++;
				}
				 temp/=10;
			}
			ans=i*n;
			if(cover==10) break;
		}
		printf("Case #%d: ",j);
		if(cover==10) printf("%lld\n",ans);
		else printf("INSOMNIA\n");
	}
	return 0;
}
