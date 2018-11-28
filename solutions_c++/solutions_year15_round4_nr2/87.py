#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>

#define eps 1e-7

#define MAXN 105

int n;
double V,X;
double R[MAXN],C[MAXN];

int list1[MAXN],list2[MAXN];

inline bool cmp(int i,int j)
{
	return C[i]<C[j];
}

double K[MAXN];
double sumR;

inline void update(int i,int j)
{
	double t1=fabs(C[i]-X)*R[i],t2=fabs(C[j]-X)*R[j];
	double tmp=std::min((1-K[i])/t2,(1-K[j])/t1);
	K[i]+=tmp*t2;
	K[j]+=tmp*t1;
}

inline void solve()
{
	scanf("%d%lf%lf",&n,&V,&X);
	int i,j;
	for (i=1;i<=n;i++) {
		scanf("%lf%lf",R+i,C+i);
	}
	if (n==1) {
		if (fabs(C[1]-X)>eps) {
			puts("IMPOSSIBLE");
		} else {
			printf("%.9lf\n",V/R[1]);
		}
		return;
	}
	int cnt1=0,cnt2=0;
	sumR=0;
	for (i=1;i<=n;i++) {
		if (fabs(C[i]-X)<=eps) {
			sumR+=R[i];
		} else if (C[i]<X) {
			list1[++cnt1]=i;
		} else {
			list2[++cnt2]=i;
		}
	}
	if (!cnt1 || !cnt2) {
		if (sumR>0) {
			printf("%.9lf\n",V/sumR);
		} else {
			puts("IMPOSSIBLE");
		}
		return;
	}
	std::sort(list1+1,list1+cnt1+1,cmp);
	std::sort(list2+1,list2+cnt2+1,cmp);
	
	memset(K,0,sizeof(K));
	
	double c1=C[list1[cnt1]];
	double c2=C[list2[1]];
	int id1=list1[cnt1];
	int id2=list2[1];
	if ((c2-X)*R[id2]>(X-c1)*R[id1]) {
		K[list1[cnt1]]=1;
		K[list2[1]]=(X-c1)*R[id1]/((c2-X)*R[id2]);
		for (i=cnt1-1;i>=1;i--) {
			for (j=1;j<=cnt2;j++) {
				update(list1[i],list2[j]);
			}
		}
	} else {
		K[list2[1]]=1;
		K[list1[cnt1]]=(c2-X)*R[id2]/((X-c1)*R[id1]);
		for (i=2;i<=cnt2;i++) {
			for (j=cnt1;j>=1;j--) {
				update(list2[i],list1[j]);
			}
		}
	}
	
	for (i=1;i<=n;i++) {
		sumR+=R[i]*K[i];
	}
	printf("%.9lf\n",V/sumR);
}

int main()
{
	int T;
	scanf("%d",&T);
	int i;
	for (i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		solve();
	}
}