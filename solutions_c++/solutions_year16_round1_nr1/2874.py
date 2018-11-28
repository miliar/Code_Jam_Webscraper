#define ll long long
#define mod 1000000007LL
#define F(a,b,c) for(a=b;a<c;a++)
#define Fr(a,b,c) for(a=b;a>=c;a--)
#define pf printf
#define sfd(a) scanf("%d",&a)
#define sfdd(a,b) scanf("%d%d",&a,&b)
#define sfl(a) scanf("%lld",&a)
#define sfll(a,b) scanf("%lld%lld",&a,&b)
#define pfd(a) printf("%d",a)
#define pfl(a) printf("%lld",a)
#define sf scanf
#define line printf("\n")
#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp(a,b) make_pair(a,b)
#define let(x,a) __typeof(a) x(a)
#define forall(it,v) for(it=v.begin();it!=v.end();it++)
int main(){
int t,k=1;
char st[1005],n[3000];
sfd(t);
while(k<=t){
	sf("%s",st);
	int i,l=strlen(st),f=1004,s=1004;
	n[f]=st[0];
	F(i,1,l) {
		if(n[f]<=st[i])
			n[--f]=st[i];
		else n[++s]=st[i];
	}
	pf("Case #%d: ",k);
	F(i,f,s+1)
		pf("%c",n[i]);
	line;
	k++;
}
return 0;
}
