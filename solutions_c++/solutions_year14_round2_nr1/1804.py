//A.cpp
//SmartCoder
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end();i++)
#define present(c,x)  ( (c).find(x) !=(c).end())
#define cpresent(c,x) (find(all(c),x)!= (c).end() )
#define minei(x)  min_element(x.begin(),x.end())-(x).begin()
#define maxei(x)  max_element(x.begin(),x.end())-(x).begin()

#define uns(v)     sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define acusum(x)  accumulate(x.begin(),x.end(),0)
#define acumul(x)  accumulate(x.begin(),x.end(),1, multiplies<int>()); 
#define bits(x)     __builtin_popcount( x )
#define oo INT_MAX
#define inf 1000000000

const double pi=acos(-1.0);
const double eps=1e-11;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
int calc(vector<int> &v){
  sort(all(v));
  int mx=v[sz(v)-1];
  int mn=mx;
  for(int i=1;i<=mx;++i){
    int ct=0;
    for(int j=0;j<sz(v);++j){
      ct+=abs(i-v[j]);
    }
    mn=min(mn,ct);
  }
  return mn;
}
string chk(string &s){
  string rs="";
  rs+=s[0];
  for(int i=1;i<sz(s);++i){
    if(s[i]==s[i-1]) continue;
    rs+=s[i];
  }
  return rs;
}
void pv(vector<int> v){
  cout<<"[ ";
  for(int i=0;i<sz(v);i++){
    cout<<v[i]<<", ";
  }
  cout<<"]"<<endl;
}
int main(){
  std::ios_base::sync_with_stdio(0);
  freopen("output.txt","w",stdout);
  freopen("A-small-attempt0.in","r",stdin);
  int tc,n;
  cin>>tc;
  string str;
  for(int T=1;T<=tc;++T){
    vector<string> s;
    set<string> st;
    cin>>n;
    for(int i=0;i<n;++i){
      cin>>str;
      s.pb(str);
      st.insert(chk(str));
    }
    if(sz(st)!=1){
      printf("Case #%d: Fegla Won\n",T);
    }else{
      vector<int> cur;
      string ss=*st.begin();
      int ct=0;
      int res=0;
      for(int i=0;i<sz(ss);++i){
        for(int j=0;j<sz(s);++j){
          ct=0;
          for(int k=0;k<sz(s[j]);++k){
            if(s[j][k]=='*')continue;
            if(s[j][k]==ss[i]){
              ct++;
              s[j][k]='*';

            }else break;
          }
          cur.pb(ct);
        }

        res+=calc(cur);
        cur.clear();
      }
      printf("Case #%d: %d\n",T,res);
    }
  }
  return 0;
}
