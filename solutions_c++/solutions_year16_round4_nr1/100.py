#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

// alphabetical : P R S
int RW[20][3], PW[20][3], SW[20][3]; // R P S
string RWS[20], PWS[20], SWS[20];
// vector<string> RWS[20], PWS[20], SWS[20];

int main(){
  RW[0][0] = 1; PW[0][1] = 1; SW[0][2] = 1;
  RWS[0] = "R"; PWS[0] = "P"; SWS[0] = "S";
  for(int n = 1; n <= 12; n++){
    // RW : RW + SW
    for(int i = 0; i < 3; i++) RW[n][i] = RW[n - 1][i] + SW[n - 1][i];
    RWS[n] = min(RWS[n - 1] + SWS[n - 1], SWS[n - 1] + RWS[n - 1]);
    /*
       if(n < 4){
       for(string r1 : RWS[n - 1]){
       for(string s1 : SWS[n - 1]){
       RWS[n].push_back(r1 + s1);
       RWS[n].push_back(s1 + r1);
       }
       }
       sort(RWS[n].begin(), RWS[n].end());
       }
     */
    // PW : PW + RW
    for(int i = 0; i < 3; i++) PW[n][i] = PW[n - 1][i] + RW[n - 1][i];
    PWS[n] = min(PWS[n - 1] + RWS[n - 1], RWS[n - 1] + PWS[n - 1]);
    /*
       if(n < 4){
       for(string p1 : PWS[n - 1]){
       for(string r1 : RWS[n - 1]){
       PWS[n].push_back(p1 + r1);
       PWS[n].push_back(r1 + p1);
       }
       }
       sort(PWS[n].begin(), PWS[n].end());
       }
     */
    // SW : SW + PW
    for(int i = 0; i < 3; i++) SW[n][i] = SW[n - 1][i] + PW[n - 1][i];
    SWS[n] = min(SWS[n - 1] + PWS[n - 1], PWS[n - 1] + SWS[n - 1]);
    /*
       if(n < 4){
       for(string s1 : SWS[n - 1]){
       for(string p1 : PWS[n - 1]){
       SWS[n].push_back(s1 + p1);
       SWS[n].push_back(p1 + s1);
       }
       }
       sort(SWS[n].begin(), SWS[n].end());
       }
     */
  }

  /*
  for(int n = 0; n <= 12; n++){
    printf("%d\n", n);
    printf("%s\n%s\n%s\n", RWS[n].c_str(), PWS[n].c_str(), SWS[n].c_str());
  }
  */

  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    int N, R, P, S; scanf("%d%d%d%d", &N, &R, &P, &S);

    printf("Case #%d: ", tt);

    // RW
    if(R == RW[N][0] && P == RW[N][1] && S == RW[N][2]){
      puts(RWS[N].c_str()); continue;
    }
    // PW
    if(R == PW[N][0] && P == PW[N][1] && S == PW[N][2]){
      puts(PWS[N].c_str()); continue;
    }
    // SW
    if(R == SW[N][0] && P == SW[N][1] && S == SW[N][2]){
      puts(SWS[N].c_str()); continue;
    }
    puts("IMPOSSIBLE");
  }
  return 0;
}
