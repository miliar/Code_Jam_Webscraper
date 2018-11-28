#include<bits/stdc++.h>
#define x first
#define y second
using namespace std;
typedef long long LL;
typedef long double LD;
const LL LLinf=9e18+5;
const int MOD=1e9 + 7;
const LD pi = acos(-1.0L);
const int NMAX = 100000+69;
const int INF = 0x3f3f3f3f;

int T, k;
string s;

void solve(){
  cin>>T;
  for(int tt=1; tt<=T; tt++){
    cin>>s; cin>>k;
    int rs = 0;
    for(int i=0; i<s.size()-k+1; i++){
      if(s[i] == '-'){
        rs++;
        for(int j=i; j<i+k; j++){
          if(s[j] == '-')
            s[j] = '+';
          else
            s[j] = '-';
        }
      }
    }
    bool q = 1;
    for(int i=1; i<=s.size(); i++){
      if(s[i-1] != '+')
        q = 0;
    }
    cout<<"Case #"<<tt<<": "<<"";
    if(!q)
      cout<<"IMPOSSIBLE"<<"\n";
    else
      cout<<rs<<"\n";
  }
}

int main()
{
  cout<<setprecision(6)<<fixed;
	ios_base::sync_with_stdio(0);
	cin.tie(0);


  solve();
	 
	return 0;
}
