#include<iostream>
#include<cstdio>
#include<algorithm>
#include<fstream>
using namespace std;
int main(){
ofstream ofs;
ofs.open("D.txt");
int t;
cin>>t;
int n;
double a[11],b[11],c[11],d[11];
for(int i=1;i<=t;i++){
cin>>n;
for(int j=0;j<n;j++){
scanf("%lf",&a[j]);

}
for(int j=0;j<n;j++){
scanf("%lf",&b[j]);
}

sort(a,a+n);
sort(b,b+n);
for(int j=0;j<n;j++){
c[j]=a[j];
d[j]=b[j];
}

	int d_c=0,n_c=0;
	
	for(int k=0;k<n;k++){
	   for(int j=0;j<n;j++){		
		if(d[k]<c[j]){
		d[k]=0;c[j]=0;d_c++;break;
		}
		//cout<<c[j]<<" "<<d[k]<<endl;
		}
	}
   
//	for(int j=0;j<n;j++)cout<<d[j]<<endl;

	for(int j=0;j<n;j++){
	for(int k=0;k<n;k++){	
	if(a[j]<b[k]){a[j]=0;b[k]=0;break;}
		}
	}
	for(int j=0;j<n;j++)
	if(a[j]!=0)
	n_c++;
	ofs<<"Case #"<<i<<": "<<d_c<<" "<<n_c<<endl;
}
return 0;
}
