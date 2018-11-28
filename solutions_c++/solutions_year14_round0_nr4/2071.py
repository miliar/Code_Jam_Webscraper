#include<iostream>
#include<algorithm>
using namespace std;
int imandar(double *nm,double* k,int n){
	int pts=n,nptr=0,kptr=0;
	while(kptr<n){
		while(k[kptr]<nm[nptr]&&kptr<n){
			kptr++;
		}
		if(kptr<n){
			pts--;
			kptr++;
			nptr++;
		}
	}
	return pts;
	
}
int chutiya(double *a,double *b,int n){
	int ptr1=0,ptr2=0,count=0;
	while(ptr1<n){
		if(a[ptr1]>b[ptr2]){
			count++;
			ptr1++;
			ptr2++;
		}
		else
		ptr1++;
	}
	return count;
}
int main(){
	int t, n;
	double naomi[1001],ken[1001];
	cin>>t;
	for(int k=1;k<=t;k++){
		cin>>n;
		for(int i=0;i<n;i++){
			cin>>naomi[i];
		}
		for(int i=0;i<n;i++){
			cin>>ken[i];
		}
		sort(naomi,naomi+n);
		sort(ken, ken+n);
		cout<<"Case #"<<k<<": ";
		cout<<chutiya(naomi,ken,n)<<" "<<imandar(naomi,ken,n)<<endl;
		
	}
}
