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
char s[200];
int main()
{
	ll t,tc=1,z,ans,i;
	scanf("%lld",&t);
	while(t--) {
		scanf("%s",s);
		printf("Case #%lld: ",tc++);
		z=strlen(s);
		ans=0;
		for(i=0;i<z;i++) {
			if(s[i]=='+')break;			
		}
		if(i==z){
			printf("1\n");
			continue;
		}
		if(i>0)ans++;
		i++;
		for(;i<z;i++) {
			if(s[i]=='+' && s[i-1]=='-')ans+=2;
		}
		if(s[z-1]=='-')ans+=2;
		printf("%lld\n",ans);
	}	






	return 0;
}
