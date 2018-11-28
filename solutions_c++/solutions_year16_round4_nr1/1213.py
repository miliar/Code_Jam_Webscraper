//Michał Glapa
#include<bits/stdc++.h>
using namespace std;
#define FOR(i,j,k) for(int i=j;i<=k;i++)
#define REP(i,n) for(int i=0;i<n;i++)
#define FORD(i,j,k) for(int i=j;i>=k;i--)
#define ll long long
//Make sure no overflow problems
#define int long long
#define pb push_back
#define x first
#define y second
#define all(x) x.begin(),x.end()
#define ld long double
#define mini(x,y) x=min(x,y)
#define maxi(x,y) x=max(x,y)
#define CLR(a,x) memset(a,x,sizeof(a))
#define SIZE(x) ((int)x.size())
const int INF = 1000000009;
const long long INFLL = (ll)INF * (ll)INF;
const ld EPS = 10e-9;
typedef vector<int> vi;
typedef pair<int,int> pii;

//reading and printing
template<typename T>
void read(T & a) {cin >> a;}
template<typename T>
void read(vector<T> & v, int n) {int tmp; REP(i,n){read(tmp); v.pb(tmp);};}
template<typename T, typename V>
void read(pair<T,V> & p) {read(p.x); read(p.y);}
template<typename T>
void print(T & a) {cout << a << "\n";}
void print(char * s) {printf("%s\n",s);}
template<typename T>
void print_(T & a) {cout << a <<" ";}
template<typename T>
void print(vector<T> &v) {for(auto &i : v) print_(i); cout<<"\n";}
template<typename T,typename V>
void print(pair<T,V> &p) {print_(p.x);print(p.y);}
template<typename T,typename V>
void print_(pair<T,V> &p) {print_(p.x);print_(p.y);}

//useful funcs
template<typename T>
void unique(vector<T> & v) {v.resize(unique(v.begin(),v.end())-v.begin());}
vi range (int a, int b) {vi res; FOR(i,a,b-1) res.pb(i); return res;}

///////////////////////////////////////////////////////////////
//

char mp[128];
string advance(string s, int n) {
  if (n == 0)
    return s;
  string b;
  b.push_back(mp[s[0]]);
  string x = advance(s, n-1);
  string y = advance(b, n-1);
  if (x > y)
    swap(x, y);
  x += y;
  return x;
}
int r, p, ss;
bool check(string s, int n) {
  s = advance(s, n);
  int cr = 0, cs = 0, cp = 0;
  for (auto i : s) {
    if (i ==  'R')
      cr++;
    if (i == 'P')
      cp++;
    if (i == 'S')
      cs++;
  }
  if (cr == r && cs == ss && cp == p) {
    cout << s << endl;
    return true;
  }
  return false;



}
main()
{
  mp['R'] = 'S';
  mp['S'] = 'P';
  mp['P'] = 'R';

  int t;
  cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    cout << "Case #" << tt << ": ";
    int n;
    cin >>n >>  r >> p >> ss;
    vector<string> l {"R", "P", "S"};
    bool found = false;
    for (auto i : l)
      if (check(i, n)) {
        found = true;
        break;
      }
    if(!found)
    cout << "IMPOSSIBLE\n";
  }

}
