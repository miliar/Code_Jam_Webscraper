#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
#define FO(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)

typedef long long ll;
ll n,p,q,r,s;
ll t[1000005];
void init()
{
	scanf("%lld%lld%lld%lld%lld",&n,&p,&q,&r,&s);
	for (int i=0;i<n;i++)
		t[i]=(long long)(i*p+q)%r+s;
	//for (int i=0;i<n;i++)
	//	printf("%lld ",t[i]);puts("");
}

ll tot;
ll mmax(ll a,ll b,ll c)
{
	return max(a,max(b,c));
}
void process()
{
	int ptr1=0,ptr2=0;
	ll s1=0,s2=t[0],s3=0;
	for (int i=1;i<n;i++)s3+=t[i];
	tot=s2+s3;

	ll mmin=max(s2,s3);
	for (;ptr1<n;ptr1++)
	{
		ll less=mmax(s1,s2,s3);
		while (ptr2+1<n&&mmax(s1,s2+t[ptr2+1],s3-t[ptr2+1])<less)
			ptr2++,s2+=t[ptr2],s3-=t[ptr2],less=mmax(s1,s2,s3);
		mmin=min(mmin,less);
		s1+=t[ptr1];
		s2-=t[ptr1];
	}
	printf("%.12lf\n",(double)(tot-mmin)/tot);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int Q;
	scanf("%d",&Q);
	for (int cnt=1;cnt<=Q;cnt++)
	{
		init();
		printf("Case #%d: ",cnt);
		process();
	}
	return 0;
}
