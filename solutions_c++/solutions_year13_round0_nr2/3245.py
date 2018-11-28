#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
using namespace std;

#define mp make_pair
#define pb push_back
#define sz(x) (int)(x).size()
#define foreach(i,x) for (__typeof(x.begin()) i = x.begin();i!=x.end();++i)
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int maxn = (int)1e5+9;
const int inf = (int)1e9+7;

#define y first
#define x second

int main(){
  #ifdef LOCAL
  freopen("err","w",stderr);
  #endif
  int t;
  scanf("%d",&t);
  for (int tc=1;tc<=t;++tc){
    int n,m;
    scanf("%d%d",&n,&m);
    int a[102][102], b[102][102];
    for (int i=1;i<=n;++i)
      for (int j=1;j<=m;++j){
        scanf("%d",&a[i][j]);
        b[i][j] = 100;
      }
    for (int i=1;i<=n;++i){
      int cat = 0;
      for (int j=1;j<=m;++j)
        cat = max(cat, a[i][j]);
      for (int j=1;j<=m;++j)
        b[i][j] = min(cat, b[i][j]);
    }
    for (int j=1;j<=m;++j){
      int cat = 0;
      for (int i=1;i<=n;++i)
        cat = max(cat, a[i][j]);
      for (int i=1;i<=n;++i)
        b[i][j] = min(b[i][j], cat);
    } 
    bool res = true;
    for (int i=1;i<=n && res;++i)
      for (int j=1;j<=m;++j)
        if (a[i][j]!=b[i][j]){
          res = false;
          break;
        }
    printf("Case #%d: %s\n", tc, (res)?"YES":"NO");
  }
	return 0;
}

