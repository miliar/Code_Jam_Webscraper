#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<utility>
#define MP make_pair
using namespace std;
typedef long long ll ;
ll a , b, ans; 
bool is_palindrome(int a){
     string x,y;
     while(a){
              x += (a%10)+'0';
              a /= 10;
     }
     y = x;
     reverse(x.begin() , x.end());
     if(x == y)return true;
     return false;
}
void find(){
     ans = 0;
     for(ll i  = (ll)sqrt(a) ; i <= (ll)sqrt(b) ; i++){
             if(i *i >= a && i*i <= b){
                  if( is_palindrome(i*i) && is_palindrome(i) )
                    // cout<<i<<" "<<i*i<<endl,
                     ans++;
             }
     }
}
int main(){
    //freopen("input", "r", stdin);
    //freopen("output" ,"w",stdout);
    int t , test = 1; 
    cin >> t;
    while( t -- ){
           cin >> a >> b;
           find();
           printf("Case #%d: %lld\n",test, ans);
           test++;
    }
    return 0 ;     
}
