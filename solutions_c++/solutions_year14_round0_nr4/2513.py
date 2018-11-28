#include <bits/stdc++.h>
const int N=1010;
double A[N],B[N];
bool flag[N];
int n;
bool want(double a){
	int idx=-1;
	double Min=1e20;
	for(int i=0;i<n;i++)
		if(flag[i]==false && B[i]>a && Min>B[i]){
			Min=B[i];
			idx=i;
		}
	if(idx==-1){
		for(int i=0;i<n;i++)
			if(flag[i]==false){
				flag[i]=true;
				break;
			}
		return false;
	}
	else{
		flag[idx]=true;
		return true;
	}
}
bool ok(int k){
	for(int i=k-1;i>=0;i--)
		if(B[i]>A[n-1+i-(k-1)])return false;
	return true;
}
int main(){
	int w=1,T;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%lf",&A[i]);
		for(int i=0;i<n;i++)
			scanf("%lf",&B[i]);
		int ans1=0,ans2=0;
		for(int i=0;i<n;i++)flag[i]=false;
		std::sort(A,A+n);
		std::sort(B,B+n);
		/*for(int i=0;i<n;i++)
			printf("%.3lf ",A[i]);
		puts("");
		for(int i=0;i<n;i++)
			printf("%.3lf ",B[i]);
		puts("");*/
		for(int i=0;i<n;i++){
			ans1+=want(A[i]);
		}
		ans1=n-ans1;
		for(int i=n;i>=1;i--){
			if(ok(i)){ans2=i;break;}
		}
		printf("Case #%d: %d %d\n",w++,ans2,ans1);
	}
}
