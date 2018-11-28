#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <limits>
#include <utility>
#include <iomanip>
#include <set>
#include <numeric>
#include <cassert>
#include <ctime>
#include <fstream>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 9223372036854775807LL
#define INF 1000000000
#define PI acos(-1.0)
#define EPS 1e-8
#define LL long long
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define setzero(a) memset(a,0,sizeof(a))
#define setdp(a) memset(a,-1,sizeof(a))

using namespace std;

multiset<pair<int, int> > e, f;

pair<int, int> gethash(string s);

vector<pair<int, int> > get(string s)
{
  vector<pair<int, int> > v;
  string tmp = "";
  for(int i=0;i<s.size();i++)
  {
    if(s[i] == ' ')
    {
      v.push_back(gethash(tmp));
      tmp = "";
    }
    else tmp+=s[i];
  }
  v.push_back(gethash(tmp));
  return v;
}

vector<vector<pair<int, int> > > arr;

int res, n;

pair<int, int> gethash(string s)
{
  int b = 41, m = mod;
  pair<int, int> res = mp(0, 0);
  for(int i=0;i<s.size();i++)
  {
    res.f = (res.f * 1LL * b + s[i] - '0') % m;
  }
  b+=2, m+=2;
  for(int i=0;i<s.size();i++)
    res.s = (res.s * 1LL * b + s[i] - '0') % m;
  return res;
}

void solve(int ind)
{
  if(ind == n)
  {
    int c = 0;
    pair<int, int> tmp = mp(-1, -1);
    for(multiset<pair<int, int> > ::iterator it = e.begin(); it != e.end();it++)
    {
      if((*it).f == tmp.f && (*it).s == tmp.s) continue;
      tmp = *it;
      if(f.find(tmp) != f.end()) c++;
    }
    res = min(res, c);
    return;
  }
  if(ind != 1)
  {
    for(int k=0;k<arr[ind].size();k++)
    e.insert(arr[ind][k]);
    int c = 0;
    pair<int, int> tmp = mp(-1, -1);
    for(multiset<pair<int, int> > ::iterator it = e.begin(); it != e.end();it++)
    {
      if((*it).f == tmp.f && (*it).s == tmp.s) continue;
      tmp = *it;
      if(f.find(tmp) != f.end()) c++;
    }
    if(c < res) solve(ind + 1);
    for(int k=0;k<arr[ind].size();k++)
      e.erase(e.find(arr[ind][k]));
  }
  if(ind)
  {
    for(int k=0;k<arr[ind].size();k++)
    f.insert(arr[ind][k]);
  int c = 0;
    pair<int, int> tmp = mp(-1, -1);
    for(multiset<pair<int, int> > ::iterator it = e.begin(); it != e.end();it++)
    {
      if((*it).f == tmp.f && (*it).s == tmp.s) continue;
      tmp = *it;
      if(f.find(tmp) != f.end()) c++;
    }
    if(c < res) solve(ind + 1);
  for(int k=0;k<arr[ind].size();k++)
    f.erase(f.find(arr[ind][k]));
  }
}

int main()
{
  ios_base::sync_with_stdio(0);
  freopen("C-small-attempt1.in", "r", stdin);
  freopen("out.txt", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    cin >> n;
    string s;
    res = INF;
    getline(cin, s);
    arr.clear();
    e.clear();
    f.clear();
    for(int i=0;i<n;i++)
    {
      getline(cin, s);
      arr.push_back(get(s));
    }
    solve(0);
    //if(res != c) cerr << "Error @ " << tt << " Expected : " << res << " Found : " << c << "\n";
    cerr << "Case #" << tt << ": done\n";
    cout << "Case #" << tt++ << ": " << res << "\n";
  }
  return 0;
}
