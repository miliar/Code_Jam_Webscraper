#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define SZ(x) ((int)(x).size())
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define max(a,b) ( (a) > (b) ? (a) : (b))
#define min(a,b) ( (a) < (b) ? (a) : (b))
#define abs(x) (x<0?(-x):x)
#define ll long long 
#define ull unsigned long long 
#define ui unsigned int
#define us unsigned short
#define pi 3.1415926535897932384626
#define pb push_back
#define mp make_pair
#define ms(s, n) memset(s, n, sizeof(s))
#define all(a) a.begin(), a.end()
#define dist(xa,ya,xb,yb) sqrt(((xa) -(xb))*((xa) -(xb)) + ((ya)- (yb))*((ya)- (yb)))

using namespace std;

inline ll Multiplymodd(ll a, ll b, ll modd) {
    ull r = 0;
    a %= modd, b %= modd;
    while (b) {
        if (b & 1LL) r = (r + a) % modd;
        b >>= 1LL, a = ((ull) a << 1LL) % modd;
    }
    return r;
}
 
inline ll Powermodd(ll a, ll n, ll modd) {
    ll r = 1LL;
    while (n) {
        if (n & 1LL) 
          r = Multiplymodd(r, a, modd);
        n >>= 1LL, a = Multiplymodd(a, a, modd);
    }
    return r;
}

inline  bool eprimo(ll n) {
    int precalc = 9, p[] = { 2, 3, 5, 7, 11, 13, 17, 19, 23 };
    for (int i = 0; i < precalc; i++)
        if (n % p[i] == 0) 
          return n == p[i];
    if (n < p[precalc - 1]) 
        return 0;
    ll s = 0, t = n - 1LL;
    while (~t & 1LL)
        t >>= 1LL, ++s;
    for (int i = 0; i < precalc; i++){
        ll pt = Powermodd(p[i], t, n);
        if (pt == 1LL) 
            continue;
        bool ok = 0;
        for (int j = 0; j < s && !ok; j++){
            if (pt == n - 1LL) ok = 1;
              pt = Multiplymodd(pt, pt, n);
        }
        if (!ok) 
            return 0;
    }
    return 1;
}
inline string converte(int n, ll A){
  string ans = "";
  for(int i = 0; i < n; i++){
       if(A & (1LL<<i)){
          ans = "1"+ans;
       } else {
          ans = "0" + ans;
       }
  }
  return ans;
}

inline ll pt(ll b, ll e){
     if(e == 0LL)
        return 1LL;
     if(e == 1LL)
        return b;
     ll ans = pt(b,e>>1LL);
     return ans*ans*pt(b,e&1LL);
}


ll divi(ll A){
   if((A% 2LL) == 0LL)
      return 2;
   if((A % 3LL) == 0LL)
      return 3;
   ll F = (ll)(sqrt((double)(A)) + 1e-7);
   for(ll i = 5; i <= F; i += 2){
         if((A%i)==0LL) 
          return i;
   }
}

int main () {
     int n,T,J,K;
     cin >> T; 
     for(int t = 1; t <= T; t++){
        cin >> n >> K;
        cout << "Case #" << t << ":" << "\n";
        for(ll j = (1LL<<(n-1))+1LL; j < (1LL<<n); j += 2LL){ 
              bool converteE = 0; 
              //cout << "merda1" << endl; 
              vector<ll> V; 
              for(int base = 2; base <= 10; base++){ 
                  ll soma = 0LL;
                  //cout << "merda2" << endl;
                  for(int h = 0; h < n; h++){
                      if(j&(1LL<<h)){ 
                           soma += pt(1LL*base,1LL*h);
                      }
                  }
                  if(eprimo(soma)){
                      converteE = 1;
                      break;
                  }else{
                      V.push_back(soma);
                  }
              }
              if(!converteE){
                  //dafuq aqui
                  cout << converte(n,j) << " ";
                  for(int i = 0; i < 9; i++){
                      cout << divi(V[i]);
                      if(i+1 != 9) 
                        cout << " ";
                  } 
                  cout << endl;
                  K--; 
                  if(K==0)
                    break;
              }
        }
     }
}