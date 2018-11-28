#include <bits/stdc++.h>
using namespace std ;
long long check[10];
main ()
{
  freopen("out1.txt","w",stdout);
    freopen("in1.txt","r",stdin);
long long t;
cin>>t;
for(int i=0 ; i <  t ; i++){
        long long n,g,ans,k;
cin>>n;
        for(int j =0 ; j < 10;j++){
            check[j]=0;
        }
bool cn=false;
long h=0;
while(cn==false){
        long long y=n;
if(y==0){
     cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
    cn=true;
}
        y=y*h;
while(y>0){
check[y%10]=1;
y/=10;
}
h++;
 g=0;
for(int j =0; j< 10 ; j++){
    if(check[j]==1){
    g++;
    }
}
if(g==10){
    cn=true;
    ans=n*(h-1);
    k=g;
    }
}
if(k==10){
    cout<<"Case #"<<i+1<<": "<<ans<<endl;
}

}

 }
