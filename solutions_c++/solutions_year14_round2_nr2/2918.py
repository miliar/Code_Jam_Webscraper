#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<map>
#include<utility>
#define mod 1000000007


using namespace std;
int main(){

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

int t,x=1;
scanf("%d",&t);

while(t--){
long long a,b,k,ans=0,j,i,flag=0;
scanf("%lld%lld%lld",&a,&b,&k);

for(i=0;i<a;i++){

for(j=0;j<b;j++){

     long long y=i&j;
     if(y<k)
     ans++;

           }



  }

printf("Case #%d: %lld\n",x++,ans);

 }




return 0;
}
