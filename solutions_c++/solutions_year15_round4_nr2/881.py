#include <iostream>
#include <sstream>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#define eps 1e-8
using namespace std;

int n;
double v[1000],r[1000],vr[1000];
double V,R,VR;

double getans(int id,double V,double VR){
	// bool ok1=((r[id]+1e-2)*V>VR),ok2=((r[n-1]-1e-2)*V<VR);

	// if (!ok1||!ok2) return -1;

	if (id==n-1) return V/v[id];

	double l=0,rr=V/v[id];
	if (r[id]>r[id+1])
		l=max(l,(VR-V*r[id+1])/v[id]/(r[id]-r[id+1]));
	if (r[id]>r[n-1])
		rr=min(rr,(VR-V*r[n-1])/v[id]/(r[id]-r[n-1]));
	// cout<<l<<' '<<rr<<endl;
	double lres=max(l,getans(id+1,V-l*v[id],VR-l*v[id]*r[id]));
	double rres=max(rr,getans(id+1,V-rr*v[id],VR-rr*v[id]*r[id]));
	double tres=min(lres,rres);
	// cout<<id<<' '<<l<<' '<<getans(id+1,V-l*v[id],VR-l*v[id]*r[id])<<endl;

	for (;(l<rr-1e-8);){
		double mi=(l+rr)/2;
		double res=getans(id+1,V-mi*v[id],(VR-mi*v[id]*r[id]));
		if (res>mi) l=mi;
		else rr=mi;
		tres=min(tres,max(res,mi));
	}
	return tres;
}

void getans(){
	scanf("%d%lf%lf",&n,&V,&R);
	VR=V*R;
	for (int i=0;i<n;i++){
		scanf("%lf%lf",&v[i],&r[i]);
		vr[i]=v[i]*r[i];
	}

	for (int i=0;i<n;i++)
		for (int j=i+1;j<n;j++)
		if (r[i]<r[j]){
			swap(r[i],r[j]);
			swap(v[i],v[j]);
		}
	if (r[0]<R-eps||r[n-1]>R+eps) printf("IMPOSSIBLE\n");
	else printf("%.20f\n",getans(0,V,VR));
}

int main(){
	int N;
	scanf("%d",&N);
	for (int r=1;r<=N;r++){
		printf("Case #%d: ",r);
		getans();
	}
	return 0;
}