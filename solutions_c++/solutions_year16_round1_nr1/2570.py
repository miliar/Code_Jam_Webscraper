#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define all(a)  a.begin(), a.end()
#define allr(a) a.rbegin(), a.rend()
#define fill(a, x) memset(a, x, sizeof(a));
#define mod 1000000007
#define _for(it, a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); ++it)

using namespace std;

string S;

string get(){
   string res = "";
   res += S[0];
   for(int n = 1; n < S.sz; ++n){
      if((res + S[n]) > (S[n] + res)) res += S[n];
      else res = S[n] + res;
   }
   return res;
}

int main() {
   int T;
   cin >> T;
   for(int test = 1; test <= T; ++test){
      cin >> S;
      printf("Case #%d: ", test);
      cout << get() << endl;
      cerr << test << endl;
   }
   return 0;
}