#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define x first
#define y second
#define fi(n) fo(i,n)
#define fj(n) fo(j,n)
#define fk(n) fo(k,n)
#define fd(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define fo(i,n) fr(i,0,n)
#define fr(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define all(x) (x).begin(),(x).end()
#define sqr(x) ((x)*(x))
#define srt(x) sort(all(x))

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;

const int INF = 1000*1000*1000+7;
const double EPS = 1e-9;
const double PI = acos(-1.0);
template<class T> int chmin(T &t, T f) { return (t>f) ? (t=f,1) : 0; }
template<class T> int chmax(T &t, T f) { return (t<f) ? (t=f,1) : 0; }

inline int getint() {
  int a;
  return scanf("%d",&a) ? a : (fprintf(stderr,"trying to read\n"),-1);
}

inline double getdouble() {
  double a;
  return scanf("%lf",&a) ? a : (fprintf(stderr,"trying to read\n"),-1);
}

int stoint (string s) {
  stringstream ss;
  int ret;
  ss << s;
  ss >> ret;
  return ret;
}

vector<string> split (string s) {
  stringstream ss;
  vector<string> ret;
  string t;
  ss << s;
  while (ss >> t)
    ret.pb(t);
  return ret;
}

const int N = 2500;
map<string,int> id;
int l[N];
int o[N];
int z[22][11];

void myCode() {
  string s;
  getline(cin,s);
  int ttt = stoint(s);
  fo(tt,ttt) {
    cerr << tt+1 << endl;
    id.clear();
    fi(N) {
      l[i] = 0;
      o[i] = 0;
    }
    getline(cin,s);
    int n = stoint(s);
    string en, fr;
    getline(cin,en);
    getline(cin,fr);
    vector<string> sen = split(en);
    vector<string> sfr = split(fr);
    fi(sz(sen)) {
      if (!id.count(sen[i]))
        id[sen[i]] = sz(id);
      l[id[sen[i]]] |= 1;
    }
    fi(sz(sfr)) {
      if (!id.count(sfr[i]))
        id[sfr[i]] = sz(id);
      l[id[sfr[i]]] |= 2;
    }
    vector<vector<string> > unk;
    fi(n-2) {
      getline(cin,s);
      unk.pb(split(s));
      fj(sz(unk[i])) {
        if (!id.count(unk[i][j]))
          id[unk[i][j]] = sz(id);
        z[i][j] = id[unk[i][j]];
      }
    }
    fi(n-2)
      fj(sz(unk[i]))
        o[z[i][j]] = l[z[i][j]];
    int best = INF;
    fi(1<<(n-2)) {
      //if (i%10000 == 0)
        //cerr << i << endl;
      fj(n-2)
        if (i&(1<<j))
          fk(sz(unk[j]))
            l[z[j][k]] |= 1;
        else
          fk(sz(unk[j]))
            l[z[j][k]] |= 2;
      int ret = 0;
      fj(sz(id))
        if (l[j] == 3)
          ret++;
      chmin(best,ret);
      fi(n-2)
        fj(sz(unk[i]))
          l[z[i][j]] = o[z[i][j]];
    }
    printf("Case #%d: %d\n",tt+1,best);
  }
}

int main () {
  srand(time(NULL));
  myCode();
  return 0;
}
