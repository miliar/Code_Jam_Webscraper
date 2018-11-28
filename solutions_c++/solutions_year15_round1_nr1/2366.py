#include <cstdio>
#include <string>
#include<iostream>
using namespace std;

int main() {
	int I,IT;
    long n,ii,ma,p,men,sum,x,z,y;
    long a[5000];
    freopen("A-large.in","r",stdin);
 freopen("platolarge.out","w",stdout);
    I=1;
    cin>>IT;
    while(I<=IT){
      //cout<<"pepe";
       cin>>n;
       
       for(ii=0;ii<n;ii++){
                           
          cin>>a[ii];
       }
       ii=0;
       y=0;
       while(ii<n-1){
          if(a[ii]>a[ii+1]){
            y=y+a[ii]-a[ii+1];
          }          
          ii++;
       }
    //  cout<<"\ny:"<<y;
       //cin>>
       
       
       //metho2
       ma=0;men=0;p=0;
       for(ii=1;ii<n;ii++){
                           
          p=a[ii-1]-a[ii];
          if(p>ma) { ma=p; men=a[ii];}
       }
       
       //cout<<"men:"<<men;
       sum=0;       
       for(ii=0;ii<n-1;ii++){
          
          if(a[ii]> ma){
             sum=sum+ma;
          }  
          else{               
             sum=sum+a[ii];
          }
       }

       cout<<"Case #"<<I<<": "<<y<<" "<<sum<<endl;
       I++;
    }
    
    cin>>IT;
	return 0;
}

