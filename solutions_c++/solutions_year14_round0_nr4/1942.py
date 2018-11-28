#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
	freopen("ip4.txt","r",stdin);
	freopen("op4.txt","w",stdout);
	int t,k=1;
	scanf("%d",&t);
	while(t--){
		int n;
		scanf("%d",&n);
		vector<double> p1(n),p2(n),a(n);
		for(int i=0;i<n;i++) scanf("%lf",&p1[i]);
		for(int i=0;i<n;i++) scanf("%lf",&p2[i]);
		int a1=0,a2=0;		
		for(int i=0;i<n;i++) a[i]=p2[i];
		sort(a.begin(),a.end());
		for(int i=0;i<n;i++){
			int p=upper_bound(a.begin(),a.end(),p1[i])-a.begin();
			if(p==n){
				a1++;
				continue;
			}
			int j=p;
			a[j]=0;			
			while(a[j-1]>0 && j>0){
				int temp=a[j];
				a[j]=a[j-1];
				a[j-1]=temp;
				j--;
			}
		}
		sort(p1.begin(),p1.end());
		sort(p2.begin(),p2.end());
		for(int i=n-1;i>=0;i--){
			int p=upper_bound(p1.begin(),p1.end(),p2[i])-p1.begin();
			if(p==n) continue;
			a2++;
			int j=p;
			p1[j]=0;			
			while(p1[j-1]>0 && j>0){
				int temp=p1[j];
				p1[j]=p1[j-1];
				p1[j-1]=temp;
				j--;
			}
		}
		printf("Case #%d: %d %d\n",k++,a2,a1);
	}
	return 0;
}
