#include <bits/stdc++.h>
using namespace std;
#define ll long long 

#define II pair <ll,ll>
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define mod 1000000007

#define chk1(a) cout<<#a<<" = "<<a<<'\n'
#define chk2(a,b) cout<<#a<<" = "<<a<<' '<<#b<<" = "<<b<<'\n'
#define chk3(a,b,c) cout<<#a<<" = "<<a<<' '<<#b<<" = "<<b<<' '<<#c<<" = "<<c<<'\n'
#define chk4(a,b,c,d) cout<<#a<<" = "<<a<<' '<<#b<<" = "<<b<<' '<<#c<<" = "<<c<<' '<<#d<<" = "<<d<<'\n'
ll f[12];
int main()
{
	ll t,tc=1,c,num,temp,d,n;
	scanf("%lld",&t);
	while(t--) {
		scanf("%lld",&n);
		printf("Case #%lld: ",tc++);
		if(n==0) {
			printf("INSOMNIA\n");
		}
		else {
			c=0;num=0;
			memset(f,0,sizeof(f));
			while(1) {
				num+=n;
				temp=num;
				while(temp>0) {
					d=temp%10;
					if(f[d]==0){
						f[d]++;
						c++;
					}
					temp/=10;
				}
				if(c==10) {
					printf("%lld\n",num);
					break;
				}	
			}
		}
	}








	return 0;
}
