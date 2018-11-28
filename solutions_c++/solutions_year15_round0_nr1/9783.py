#include<bits/stdc++.h>
using namespace std ;

int main(){
    ios::sync_with_stdio(false);
    int t,q ;
    cin >> t ;

for(q=1;q<=t;q++){
    int i,j,k,ans,sum,smax     ;
    string s ;
    cin >> smax   ;
    cin >> s ;
    int a[smax + 1]  ;
    for(i=0;i<=smax;i++){
    a[i]= (int)(s[i] - 48) ;
    }
  sum = a[0] ; ans  = 0 ;

  for(i=1;i<=smax;i++){

    if(sum>=i){
        sum += a[i] ;
    }
    else if(sum<i ){

        ans +=  i - sum ;
        sum = a[i] + i ;
    }

    }
    cout << "Case #" << q << ": " << ans << endl ;}
}
