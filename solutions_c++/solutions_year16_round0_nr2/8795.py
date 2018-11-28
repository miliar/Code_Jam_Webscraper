#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define REP(i, n) FOR(i, 0, n)
#define BACK(i, n) ROF(i, 0, n)
#define FOR(i, a, b) for (ll i = (a); i < (b); i++)
#define ROF(i, a, b) for (ll i = (b); --i >= (a); )
#define REP1(i, n) FOR(i, 1, n+1)
typedef pair<int, int> pii;
typedef pair<string, int> psi;
#define fi first
#define se second

ll rl()
{
  ll x;
  scanf("%lld", &x);
  return x;
}

string rs()
{
 	string x;
  cin >> x;
  return x;
}

char reverse(char c);
bool check(string& s);
bool starting(string& s);
ll findEnd(string& s ,ll l);
void flip(string& s , ll mi);
ll counting(string& s);
int main(){
	ll cases = rl();
	REP1(cc , cases){
		string s = rs();
    ll n = s.length();
    ll ans = counting(s); 
    printf("Case #%lld: %lld\n", cc, ans);
	}
}

char reverse(char c){
  if(c == '-')
    return '+';
  else 
    return '-' ;
}

bool check(string& s){
  ll length = s.length();
  for(ll i=0 ; i < length ; i++){
    if(s[i]=='-')
      return false ;
  }
  return true ;
}

bool starting(string& s){
  ll i = 0 ;
  ll length = s.length();
  while(i < length){
    if(s[i]=='+'){
      s[i]='-' ;
      i++;
    }
    else 
      break;
  }
  return (i != 0) ;
}
ll findEnd(string& s ,ll l){
  for(ll i=l;i>=0;i--){
    if(s[i]=='-')
      return i ;
  }
  return -1;
}
void flip(string& s , ll mi){
  string tmp = s;
  for(ll j=0;j<=mi;j++){
    tmp[j] = reverse(s[mi-j]) ;
  }
  s = tmp ;
  return  ;
}

ll counting(string& s){
    ll end = s.size()-1 ;
    ll first = 0 ;
    ll count = 0  ;
    while(end >= first){
        if(check(s))
          break ;
        if(starting(s))
          count++ ;
        end = findEnd(s ,end);
        if(end == -1)
          break ;
        flip(s,end);
        count++ ;
    }
    return count;
}