#include <iostream>
#include<algorithm>
using namespace std;

int main() {
	int j,k,n,i,t,w=0,dw=0;
	float a[100],b[100];
	cin>>t; 
	for(k=1;k<=t;k++){
	cin>>n; w=dw=0;
	for(i=0;i<n;i++)cin>>a[i];
	for(i=0;i<n;i++)cin>>b[i];
	sort(a,a+n);
	sort(b,b+n);
	i=j=n-1;
	while(i>=0&&j>=0){
	 if(a[i]<b[j]){i--;j--;}
	 else {i--;w++;}
	 }
	 
	i=j=n-1; 
	while(i>=0&&j>=0){
	 if(a[i]<b[j]){j--;}
	 else {i--;j--;dw++;}
	 }
	
	cout<<"Case #"<<k<<": "<<dw<<" "<<w<<endl;
	}	
	
	return 0;
}
