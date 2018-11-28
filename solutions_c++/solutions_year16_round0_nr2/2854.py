#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
string s;
void ulta(int L,int R) {
  for(int i=L;i<R;i++) {
    if(s[i] == '+') s[i] = '-';
    else s[i] = '+';
  }
}
int main() {
  freopen("B-large.in","r",stdin);
  freopen("ans.txt","w",stdout);
  int TC;
  cin >> TC;
  for(int cas=1;cas<=TC;cas++) {
    printf("Case #%d: ",cas);
    cin >> s;
    int N = s.length();
    int res = 0;
    while(true) {
       int cnt = 0;
       for(int i=0;i<N;i++) if(s[i] == '+') cnt++;
       if(cnt == N) break;
       int cntPos = 0, cntNeg = 0;
       for(int j=0;j<N;j++) {
         if(s[j] == '+') {
           if(cntNeg > 0) {
              ulta(0,j);
              res++;
              break;
           }
           else {
              cntPos++;
           }
         }
         else {
           if(cntPos > 0) {
             ulta(0,j);
             res++;
             break;
           }
           else {
             cntNeg++;
           }
         }
       }
       if(cntNeg == N) {
        ulta(0,N);
        res++;
       }
    }
    cout << res << endl;
  }
  return 0;
}
