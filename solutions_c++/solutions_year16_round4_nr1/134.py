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

int N, R, P, S;
string bet[13][3];
int bnum[13][3][3];

void pre()
{
  bet[0][0] = "R";
  bet[0][1] = "P";
  bet[0][2] = "S";

  for(int i=1; i<=12; i++)
  {
    for(int j=0; j<3; j++)
    {
      int k = (j+2) % 3;
      string s1 = bet[i-1][j] + bet[i-1][k];
      string s2 = bet[i-1][k] + bet[i-1][j];
      bet[i][j] = min(s1, s2);
    }
  }

  for(int i=0; i<=12; i++)
  {
    for(int j=0; j<3; j++)
    {
      for(auto c: bet[i][j])
      {
        if(c == 'R') bnum[i][j][0]++;
        if(c == 'P') bnum[i][j][1]++;
        if(c == 'S') bnum[i][j][2]++;
      }
    }
  }
}

int main() {
  IOS;

  pre();

  int T;
  cin>>T;
  for(int t=1; t<=T; t++)
  {
    cin>>N>>R>>P>>S;

    string ans = "IMPOSSIBLE";
    for(int i=0; i<3; i++)
      if(bnum[N][i][0] == R and bnum[N][i][1] == P and bnum[N][i][2] == S)
        ans = bet[N][i];

    cout<<"Case #"<<t<<": "<<ans<<endl;
  }

  return 0;
}
