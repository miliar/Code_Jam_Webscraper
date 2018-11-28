#include<iostream>
#include<string>
using namespace std;
int main(){
int t,n;
cin>>t;
char  s[1003];
int a[1023];
for(int i=1;i<=t;i++){
        int resilt=0,p,m=0,mk=0;
    cin>>n;
    cin>>s;
    for(int ii=0;ii<n+1;ii++)
        a[ii] = (int)(s[ii] - '0');

            //if(a[0]== 0)
                resilt= a[0];

   for(int ii=1;ii<n+1;ii++){
        if(a[ii]==0)
        continue;
   else{
if(ii<=resilt ){
    resilt = resilt + a[ii];
//cout<<resilt<<endl;
}
else{
  
     p = ii - resilt;
     resilt = resilt + p + a[ii];
     mk = mk + p;
     //cout<<resilt<<endl;

}
   }
   }

    cout<<"Case #"<<i<<":"<<" "<<mk<<endl;

}



return 0;
}
