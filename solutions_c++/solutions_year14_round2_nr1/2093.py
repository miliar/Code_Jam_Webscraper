#include <iomanip>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <math.h>

#define FR(i,en) for(int i=0; i<(en); i++)
#define FRR(i,en) for(int i=(en-1); i>=0; i--)
#define FOR(i,st,en) for(int i=(st); i<(en); i++)
#define FORR(i,st,en) for(int i=(en-1); i>=(st); i--)
#define FRI(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

#define ALL(c) (c).begin(), (c).end()
#define SZ(i) i.size()
#define SORT(c) sort(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define PI 3.1415926535897932384626433832795

typedef long long ll;
using namespace std;

char vc[100][100];
int counts[100][100];
double avg[100];

int main()
{
  cout << setiosflags(ios::fixed) << setprecision(10);  //correct double
  int tcn, N, M, MM,res;
  bool canwin;
  string s;
  cin >> tcn;
  FR(tc,tcn) {
    cout << "Case #" << tc + 1 << ": ";
    cin >> N;
    canwin=true;
    MM=0;
    FR (i,N) {
      cin >> s;
      M=0;
      FR (j,SZ(s)) {
        if (j==0 || s[j]!=s[j-1]) {
          vc[i][M]=s[j];
          if (canwin && i>0) canwin=vc[i][M]==vc[i-1][M];
          counts[i][M]=1;
          M++;
        }
        if (j>0 && s[j]==s[j-1])  counts[i][M-1]++;
      }
      MM=max(MM,M);
      if (MM!=M) canwin=false;
    }
    if (canwin) {
      FR (j,M) {
        avg[j]=0;
        FR(k,N) avg[j]+=(double)counts[k][j];
        avg[j]/=N;
        //cout << avg[j]<<' ';
      }
      res=0;
      FR(k,N) {
        FR (j,M) {
          //cout << counts[k][j] << ' ';
          res+=abs(counts[k][j]-(int)(avg[j]+0.5));
         }
      }
      cout <<res<< "\n";
    }
    else cout << "Fegla Won\n";
  }
}
