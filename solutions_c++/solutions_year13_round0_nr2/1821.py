#include <stdio.h>
#include <string.h>
#include <set>
#include <vector>

using std::set;
using std::vector;

int n, m;
int map[110][110];
bool mat[110][110];
set<int> H;
vector<int> sh;

bool check() {
  for(int i=0;i<n;++i)
    for(int j=0;j<m;++j)
      if(!mat[i][j])
        return false;
  return true;
}

bool find_answer() {
  for(set<int>::iterator it=H.begin();it != H.end();++it)
    sh.push_back(*it);
  for(int p=0;p<sh.size();++p) {
    int h = sh[p];
    for(int i=0;i<n;++i)
      for(int j=0;j<m;++j)
        if(map[i][j] == h) {
          int count = 0;
          for(int k=0;k<n;++k)
            if(mat[k][j] || map[k][j] == h)
              ++count;
          if(count >= n) {
            mat[i][j] = true;
            continue;
          }
          count = 0;
          for(int k=0;k<m;++k)
            if(mat[i][k] || map[i][k] == h)
              ++count;
          if(count >= m) {
            mat[i][j] = true;
            continue;
          }
          return false;
        }
  }
  return true;
}

int main() {
  int t, kas = 0;

  scanf("%d", &t);
  while(t--) {
    sh.clear();
    H.clear();
    
    scanf("%d%d", &n, &m);
    for(int i=0;i<n;++i)
      for(int j=0;j<m;++j) {
        scanf("%d", &map[i][j]);
        mat[i][j] = false;
        H.insert(map[i][j]);
      }
    
    bool suc = find_answer();

    if(suc) printf("Case #%d: YES\n", ++kas);
    else    printf("Case #%d: NO\n", ++kas);
  }

  return 0;
}

