#include <iostream>
#include <sstream>
#include <cstdio>
#include <string>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

#define INF (1<<29)
#define eps 1e-9

#define ll long long
#define ld long double
#define ull unsigned long long

#define mp make_pair
#define pb push_back

#define Clear(t) memset((t), 0, sizeof(t))
#define Clear2(t, v) memset((t), (v), sizeof(t))

#define For(i,a,b) for(int i = (int)(a), _t = (int)(b); i <= _t; i++)
#define Ford(i,a,b) for(int i = (int)(a), _t = (int)(b); i >= _t; i--)

ll A, B;
ll aa;
ll a;

int countDigit(ll x){
   if(x==0) return 1;
   
   int res = 0;
   while(x>0){
      x = x/10;
      ++res;
   }
   return res;
}
ll pow10(int x){
   ll res = 1;
   For(i, 1, x)   res *= 10;
   
   return res;
}

ll getPalindrome1(ll x){
   if(x==0) return 0;
   
   ll res = x;
   
   x = x/10;
   while(x>0){
      res = res * 10 + (x%10);
      x = x/10;   
   }
   
   return res;
}

ll getPalindrome2(ll x){
   if(x==0)  return -1;
   
   ll res = x;
   
   while(x>0){
      res = res * 10 + (x%10);
      x = x/10;
   }  
    
   return res;
}

string toString(ll x){
   stringstream sout;
   sout << x;
   return sout.str();
}
bool isPalindrome(ll x){
   string str = toString(x);
   
   int n = str.size();
   For(i, 0, n/2){
      if(str[i] != str[n-1-i])   return false;
   }
   
   return true;
}

int solve(){
   int cnt = 0;
   
   aa = (ll)sqrt(A); 
   
   int p = countDigit(aa);
   a = aa / pow10(p/2 + 1);
      
   //cout << "A = " << A << ", B = " << B << endl;
   //cout << "aa = " << aa << ", a = " << a << endl;
   
   ll sPa, bPa;
   For(i, a, B){
      sPa = getPalindrome1(i);   
      bPa = sPa * sPa;           //cout << "sPa = " << sPa << " => bPa = " << bPa << endl;
      if(bPa > B) break;
            
      if(sPa != -1 && A <= bPa && bPa <= B && isPalindrome(bPa))   ++cnt;                  
      
      sPa = getPalindrome2(i);
      bPa = sPa * sPa;           //cout << "sPa = " << sPa << " => bPa = " << bPa << endl;                 
      
      if(sPa != -1 && A <= bPa && bPa <= B && isPalindrome(bPa))   ++cnt;             
   }
   
   return cnt;
}

int main(){
   //freopen("input.txt", "rt", stdin);
	freopen("C-small-attempt1.in", "rt", stdin); 
	//freopen("A-large.in", "rt", stdin);     
   freopen ("output.txt","w",stdout);
	
	int sotest;   cin >> sotest;
	For(run, 1, sotest){   cout << "Case #" << run << ": ";
      cin >> A >> B;
      
      cout <<  solve() << endl;
   }
	
	return 0;
}


