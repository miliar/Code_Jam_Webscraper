#include<iostream>

using namespace std;

typedef long long ll;

bool isPalindrome(ll n){

 string s = "";

 while(n){
   s += n%10+'0';
   n/=10;
 }

 for(int i = 0; i < (int)s.length()/2; i++)
   if(s[i] != s[s.length()-i-1]) return false;

 return true;
}

int solve(ll a, ll b){

 ll ans = 0;

 for(ll i = 1; i*i <= b; i++){
   if(i*i < a) continue;
   if(isPalindrome(i*i) && isPalindrome(i)) ans++;
 }
 return ans;
}

int main(){

 int T;
 cin >> T;

 for(int i = 0; i < T; i++){
   cout << "Case #" << i+1 << ": ";
   ll a,b;
   cin >> a >> b;
   cout << solve(a,b) << endl;
 }
 return 0;

}

