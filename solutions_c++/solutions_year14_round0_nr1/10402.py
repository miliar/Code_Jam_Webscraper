#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

int main() {
  int T, r1, r2, a, ans;
  cin >> T;

  for(int t=1; t<=T; t++) {
    int cnt=0;
    vector<bool> V(17,0);

    cin >> r1;
    for(int i=1; i<=4; i++)
      for(int j=1; j<=4; j++) {
        cin >> a;
        if(i==r1) V[a] = 1;
      }

    cin >> r2;
    for(int i=1; i<=4; i++)
      for(int j=1; j<=4; j++) {
        cin >> a;
        if(i==r2) {
          if (V[a]) {
            cnt ++;
            ans = a;
          }
        }
      }

    printf("Case #%d: ", t);
    if(cnt==0) printf("Volunteer cheated!\n");
    if(cnt==1) printf("%d\n", ans);
    if(cnt>1) printf("Bad magician!\n");
  }
  
  return 0;
}

