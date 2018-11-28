#include<iostream>
using namespace std;
#include<algorithm>

int main(){

int y,t,n,i,j,c[1001],d[1001];
double a[1001],b[1001];
cin >>t;
y=t;

while(t--){
int ans1=0,ans2=0;
cin >>n;

for(i=0;i<n;++i){
c[i]=0;
d[i]=0;
}

for(i=0;i<n;++i)
cin>>a[i];

for(i=0;i<n;++i)
cin>>b[i];

sort(a,a+n);
sort(b,b+n);

for(i=n-1;i>=0;--i){
int lool=0;
for(j=n-1;j>=0;--j){

if(a[i]>b[j] && d[j]!=-1){
d[j]=-1;
lool=1;
break;
}
}
if(lool==0)
ans1++;

}



for(i=n-1;i>=0;--i){
int lol=0;
for(j=0;j<n;++j){

if(a[i]<b[j] && c[j]!=-1){
c[j]=-1;
lol=1;
break;
}
}
if(lol==0)
ans2++;

}

//cout <<" ans 1 "<<ans1 <<" "<<ans2 ;
cout << "Case #" << y-t <<": "<<n-ans1 <<" "<<ans2<<"\n";;

}




return 0;
}
