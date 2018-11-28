#include <bits/stdc++.h>
using namespace std;
bool cmp(double a,double b){return a>b;}
int main(){
	int t;
	cin>>t;
	for(int ii=1;ii<=t;ii++){
		int n;
		cin>>n;
		double a[n];
		double b[n];
		int i;
		for(i=0;i<n;i++)
			cin>>a[i];
		for(i=0;i<n;i++)
			cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		int j;
		int ans1=0,ans2=0;
		int k1=0,k2=n-1;
		for(i=n-1;i>=0;i--){
			if(a[i]>b[k2]){
				k1++;
				ans2++;
			}
			else{
				k2--;
			}
		}
		k1=0,k2=n-1;
		for(i=n-1;i>=0;i--){
			if(a[k2]>b[i]){
				k2--;
				ans1++;
			}
			else{
				k1++;
			}
		}
		printf("Case #%d: %d %d\n",ii,ans1,ans2);

	}
}