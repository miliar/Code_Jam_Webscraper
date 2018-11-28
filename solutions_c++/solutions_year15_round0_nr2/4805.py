#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define MAX 1000000007
ll a[10005];
int main(){
//long t,n,d,max,i;
ll i , j , k ,t, l , m , n,d ,max1,max2,res,cost;
cin >> t ;

for(j = 1 ; j <= t ; j++){
   n = 0;
   cin >> d;
   max1 = INT_MIN;
   for(i=0;i<d;i++){
    cin >> k ;
    a[i]=k;
    max1=max(max1,k);
   }
   res = max1;
   cost = 0;
  ll ans = 0;
  ll now = 0;
  for( i = 1 ; i <= max1 ; i++){
    max2 = INT_MIN;
    now = 0;
    for(int y = 0 ; y < d ; y++){
        if(a[y]>i){
            now+=(a[y]/i)+((a[y]%i==0)?-1:0);
            max2=max(max2,i);
        }
        else{
            max2=max(max2,a[y]);
        }
    }
    now+=max2;
    if(now<res){
        res=now;
    }

  }
   cout << "Case #"<<j<<": "<<res<<endl;
}
return 0;
}