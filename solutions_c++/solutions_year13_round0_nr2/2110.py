#include <iostream>
#include <set>
#include <map>
#include <string>
#include <vector>

using namespace std;

typedef pair<int, int> pii;
const int maxn = 100+5;
int b[maxn][maxn];
int left;
int n, m;

pii getMin() {
  int res = 12345678;
  pii pos = make_pair(-1, -1);
  for(int i=0; i<n; i++)
    for(int j=0; j<m; j++)
      if(b[i][j] != -1 && b[i][j]<res) {
        res = b[i][j];
        pos = make_pair(i, j);
      }
  return pos;
}

int doIt(int i, int j, int di, int dj, int val) {
  int rem = 0;
  for(; i<n && j<m; i+=di, j+=dj) {
    if(b[i][j]!=-1 && val!=b[i][j])
      return -1;
    rem += b[i][j] != -1;
  }
  if (rem==0) return -1;
  return rem;
}

void hashIt(int i, int j, int di, int dj) {
  for(; i<n && j<m; i+=di, j+=dj) 
    b[i][j] = -1;
}

int doIt() {
  pii pos = getMin();
  int i= pos.first;
  int j= pos.second;
  int val = b[i][j];
  int res;

  //row 
  res = doIt(i, 0, 0, 1, val);
  if(res!=-1) {
    hashIt(i, 0, 0, 1);
    return res;
  }
  //col
  res = doIt(0, j, 1, 0, val);
  if(res!=-1) {
    hashIt(0, j, 1, 0);
    return res;
  }

  return -1;
}

int main() {
  int tc;
  cin>> tc;

  for(int t=1; t<=tc; t++) {
    cin>>n>>m;
    for(int i=0; i<n; i++)
      for(int j=0; j<m; j++)
        cin>>b[i][j];

    int lft = n*m;
    bool fuck = false;
    while (lft) {
      int rem = doIt();
      if(rem==-1) {fuck=true; break;}
      lft -= rem;
    }
  
    cout<< "Case #"<<t<<": "<< (fuck?"NO":"YES")<<endl;

  }
  return 0;
}
