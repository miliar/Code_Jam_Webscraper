#include <iostream>
using namespace std;
string a[30][2];
bool b[30];
int n,best;
void f(int p,int c) {
  if (p==n) {
    if(c>best) {
      bool g=true;
      for (int i=0;i<n;i++) {
        if (b[i]) {
          g=false;
          for (int j=0;j<n;j++) {
            if (b[j]==false && a[j][0]==a[i][0]) {
              g=true;
              break;
            }
          }
          if (g==false) {
            break;
          }
          g=false;
          for (int j=0;j<n;j++) {
            if (b[j]==false && a[j][1]==a[i][1]) {
              g=true;
              break;
            }
          }
          if (g==false) {
            break;
          }
        }
      }
      if (g) {
        best = c;
      }
    }
  } else {
    b[p]=true;
    f(p+1,c+1);
    b[p]=false;
    f(p+1,c);
  }
}
int main() {
  int cases;
  cin>>cases;
  for (int z=1;z<=cases;z++) {
    cin>>n;
    best=0;
    for (int i=0;i<n;i++) {
      cin>>a[i][0]>>a[i][1];
    }
    f(0,0);
    cout<<"Case #"<<z<<": "<<best<<endl;
  }
  return 0;
}
