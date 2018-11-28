#include<iostream>
#define MAX(a,b) ((a)>(b)?(a):(b))


using namespace std;

int ar[101][101];
int R[101];
int C[101];
int main() {
  int cas;
  cin>>cas;
  for(int ca = 1; ca<=cas; ++ca) {
    int n,m;
    cin>>n>>m;
    memset(R, 0, sizeof(R));
    memset(C, 0, sizeof(C));
    for(int i=0 ;i<n; ++i) {
      for(int j=0 ;j<m; ++j) {
        cin>>ar[i][j];
        R[i] = MAX(R[i], ar[i][j]);
        C[j] = MAX(C[j], ar[i][j]);
      }
    }
    bool found = false;
    for(int i=0 ;!found && i<n; ++i) {
      for(int j=0 ;!found && j<m; ++j) {
        if (ar[i][j] != R[i] && ar[i][j] != C[j]) {
          found = true;
        }
      }
    }
    cout<<"Case #"<<ca<<": "<<(found?"NO":"YES")<<endl;
  }
}
