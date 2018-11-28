#include<iostream>
using namespace std;
int n,a[1010]; 
int solve();
int main(){
	freopen("a.txt","r",stdin);
	freopen("c.txt","w",stdout);
	int T,k;
	cin>>T;
	for(k=1;k<=T;k++){
		cin>>n;
		for(int i=0;i<n;i++) cin>>a[i];
		cout<<"Case #"<<k<<": "<<solve()<<endl;
	}
	return 0;
}
void swap(int &a,int &b){
	int t;
	t=a; a=b; b=t;
}
int solve(){
	int i,k,mi,l,r,s;
	s=0; l=0; r=n-1;
	for(k=0;k<n;k++){
		for(i=mi=l;i<=r;i++)
			if(a[i]<a[mi]) mi=i;
		if(mi-l<r-mi){
			for(i=mi;i>l;i--) swap(a[i],a[i-1]),s++;
			l++;
		}
		else{
			for(i=mi;i<r;i++) swap(a[i],a[i+1]),s++;
			r--;
		}
	}
	return s;
}
