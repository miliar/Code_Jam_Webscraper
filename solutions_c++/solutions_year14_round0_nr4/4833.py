#include <iostream>
using namespace std;
int main() {
	int t,n,i,j,k,k1,p=1;
    double a1[10],a2[10],t1;
    cin>>t;
    while(t--){
    k=0;k1=0;
    cin>>n;
    for(i=0;i<n;i++){
     cin>>a1[i];
     for(j=0;j<i;j++){
       if(a1[i]<a1[j]){
         t1=a1[i];
         a1[i]=a1[j];
         a1[j]=t1;
       }
      } 
     }
     for(i=0;i<n;i++){
     cin>>a2[i];
      for(j=0;j<i;j++){
       if(a2[i]<a2[j]){
         t1=a2[i];
         a2[i]=a2[j];
         a2[j]=t1;
       }
      } 
     }
     i=n-1;j=n-1;
     while(i>=0){
       if(a1[i]<=a2[j]){
        k++;
        i--;j--;
       }
      else
      i--;
     }
      i=n-1,j=n-1;
     while(j>=0){
     if(a1[i]>a2[j]){
      k1++;
      i--;j--;
     }
     else 
      j--;
     }
     cout<<"Case #"<<p++<<": "<<k1<<" "<<n-k<<endl;
    }
	return 0;
}