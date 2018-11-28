#include<bits/stdc++.h>
#include<unistd.h>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define F first
#define S second
#define PB push_back
#define ALL(x) begin(x),end(x)
#define SZ(x) ((int)(x).size())
#define IOS ios_base::sync_with_stdio(0); cin.tie(0)
template<typename A, typename B>
ostream& operator <<(ostream &s, const pair<A,B> &p) {
  return s<<"("<<p.first<<","<<p.second<<")";
}
template<typename T>
ostream& operator <<(ostream &s, const vector<T> &c) {
  s<<"[ ";
  for (auto it : c) s << it << " ";
  s<<"]";
  return s;
}
// Let's Fight!

const int MAXN = 20202;

int N;
string s;
int prv[MAXN], nxt[MAXN];

int calc()
{
  int cur = 0;
  
  for(int i=0; i<N; i++)
  {
    prv[i] = i - 1;
    nxt[i] = i + 1;
  }

  set<int> st;
  for(int i=0; i<N; i++)
  {
    if(nxt[i] != N and s[i] == s[nxt[i]])
      st.insert(i);
  }
  while(!st.empty())
  {
    int x = *st.begin();
    int y = nxt[x];
    int z = nxt[y];
    int w = prv[x];

    cur++;

    st.erase(x);
    st.erase(y);
    if(w != -1)
      nxt[w] = z;
    if(z != N)
      prv[z] = w;
    if(w != -1 and z != N and s[w] == s[z])
      st.insert(w);
  }

  return 5 * (N/2 + cur);
}

int main() {
  IOS;

  int T;
  cin>>T;
  for(int t=1; t<=T; t++)
  {
    cin>>s;
    N = SZ(s);
    int ans = calc();
    cout<<"Case #"<<t<<": "<<ans<<endl;
  }

  return 0;
}
