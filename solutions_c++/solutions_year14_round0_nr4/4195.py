#include<bits/stdc++.h>
using namespace std;
#define F(n) FO(i,n)
#define FO(i,n) FI(i,0,n)
#define FI(i,f,l) for(int i=(f),ei=(l);i<ei;i++)
const int mn=1e3;
double a[mn],b[mn];
int main(){
	//freopen("i.txt","r",stdin);
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int t;cin>>t;
	F(t){
		int n;cin>>n;
		F(n)cin>>a[i];
		F(n)cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		int ans1=0,ans2=0;
		for(int pa=0,pb=0;pa<n&&pb<n;){
			if(a[pa]<b[pb]){
				pa++;
			}else{
				ans1++;
				pa++;
				pb++;
			}
		}
		for(int pa=n-1,pb=n-1;0<=pa&&0<=pb;){
			if(a[pa]<b[pb]){
				ans2++;
				pa--;
				pb--;
			}else{
				pa--;
			}
		}
		//F(n)printf("%.2f%c",a[i]," \n"[i==n-1]);
		//F(n)printf("%.2f%c",b[i]," \n"[i==n-1]);
		printf("Case #%i: %i %i\n",i+1,ans1,n-ans2);
	}
	return 0;
}
