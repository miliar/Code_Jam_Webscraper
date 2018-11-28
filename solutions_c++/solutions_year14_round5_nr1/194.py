
#include <bits/stdc++.h>
using namespace std;

#define LL long long

int T;
int N,p,q,r,s;
LL sum;
LL a[1048576];
LL c[1048576];
int ll[1048576];

LL work1() {
	c[0]=a[0];
	int now=0;
	for (int i=1;i<N;i++) c[i]=c[i-1]+a[i];
	for (int i=0;i<N;i++) {
		while (now<N-1 && c[now+1]-c[i]<=c[i]) now++;
		if (c[N-1]-c[now]<=c[i]) return c[i];
	}
	return 0;
}

LL work2() {
	c[0]=0;
	for (int i=1;i<=N;i++) c[i]=c[i-1]+a[i-1];
	int now=1;
	for (int i=1;i<=N;i++) {
		while (c[now]-c[i-1]<c[i-1]) now++;
		ll[i]=now;
	}
	now=1;
	while (c[N]-c[now]>c[now]) now++;
	for (int i=1;i<=N;i++) {
		while (c[N]-c[now]>c[now]-c[i-1]) now++;
		ll[i]=max(ll[i],now);
	}
	LL ans=1e18;
	for (int i=1;i<=N;i++) {
		ans=min(ans,c[ll[i]]-c[i-1]);
	}
	return ans;
}

int main() {
	freopen("inl.txt","r",stdin);
	freopen("outl.txt","w",stdout);
	scanf("%d",&T);
	for (int ww=1;ww<=T;ww++) {
		printf("Case #%d: ",ww);
		scanf("%d%d%d%d%d",&N,&p,&q,&r,&s);
		sum=0;
		for (int i=0;i<N;i++) a[i]=(((LL)i * (LL)p + (LL)q) % (LL)r + (LL)s),sum+=a[i];
		LL a1=work1();
		LL a2=work2();
		reverse(a,a+N);
		LL a3=work1();
		LL ans=min(a1,min(a2,a3));
		printf("%.12lf\n",(double)(sum-ans)/sum);
	}
	return 0;
}
