#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <climits>
#include <cstdio>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
using namespace std;
#define db(a) (cout << (#a) << " = " << (a) << endl)
typedef long long ll;

tuple<int,int,int> sol;

map<pair<string,int>, pair<tuple<int,int,int>, string>> M;

pair<tuple<int,int,int>, string> pr(int n);
pair<tuple<int,int,int>, string> ps(int n);

pair<tuple<int,int,int>, string> rs(int n)
{
  if(M.count(make_pair("RS",n)) > 0)
  {
     return M[make_pair("RS",n)];  
   }
  if(n<=1) return make_pair(make_tuple(1,1,0), "RS");
   auto l = ps(n-1);
  auto r = rs(n-1);
  if(r.second < l.second) swap(l,r);
  l.second += r.second;
  l.first = make_tuple(get<0>(l.first)+get<0>(r.first),get<1>(l.first)+get<1>(r.first),get<2>(l.first)+get<2>(r.first));
  M[make_pair("RS",n)] = l;
  return l;
} 

pair<tuple<int,int,int>, string> ps(int n)
{
  if(M.count(make_pair("PS",n)) > 0)
  {
     return M[make_pair("PS",n)];
   }
  if(n<=1) return make_pair(make_tuple(0,1,1), "PS");
  auto l = pr(n-1);
  auto r = ps(n-1);  
  if(r.second < l.second) swap(l,r);
  l.second += r.second;
  l.first = make_tuple(get<0>(l.first)+get<0>(r.first),get<1>(l.first)+get<1>(r.first),get<2>(l.first)+get<2>(r.first));
  M[make_pair("PS",n)] = l;
  return l;
} 

pair<tuple<int,int,int>, string> pr(int n)
{
  if(M.count(make_pair("PR",n)) > 0)
  {
     return M[make_pair("PR",n)];
   }
  if(n<=1) return make_pair(make_tuple(1,0,1), "PR");
  auto l = pr(n-1);
  auto r = rs(n-1);
  if(r.second < l.second) swap(l,r);
  l.second += r.second;
  l.first = make_tuple(get<0>(l.first)+get<0>(r.first),get<1>(l.first)+get<1>(r.first),get<2>(l.first)+get<2>(r.first));
  M[make_pair("PR",n)] = l;
  return l;
} 

int main()
{
  ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
  int T;
  cin>>T;
  for(int tt=0;tt<T;tt++)
  {
    int N,R,P,S;
    cin>>N>>R>>P>>S;
    //M.clear();
    sol = make_tuple(R,S,P);
    pair<tuple<int,int,int>, string> out;
    int outi=-1;
    auto erg = pr(N);
    if(erg.first == sol)
    {
      out = erg;
      outi=0;      
      /*cout << "Case #" << tt+1 << ": " << erg.second << "\n";
      continue;*/
    }
    erg = ps(N);
    if(erg.first == sol)
    {
      if(outi==-1 || erg.second < out.second) {outi=0; out = erg;}
     /* cout << "Case #" << tt+1 << ": " << erg.second << "\n";
      continue;*/
    } 
    erg = rs(N);
    if(erg.first == sol)
    {
      if(outi==-1 || erg.second < out.second) {outi=0; out = erg;}
    /*  cout << "Case #" << tt+1 << ": " << erg.second << "\n";
      continue;*/
    }  
if(outi==-1)    cout << "Case #" << tt+1 << ": IMPOSSIBLE\n";
else cout << "Case #" << tt+1 << ": " << out.second << "\n";
  }
  return 0;
}
