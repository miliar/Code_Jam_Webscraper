#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>

using namespace std;

int order[10] = {0, 2, 4, 6, 8, 5, 1, 9, 7, 3};
string B[10]= {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
char A[10240];
int D[10][26];
int C[26];

int main(){
    for (int i = 0; i < 10; i++) {
       for (int j = 0; j < 26; j++) D[i][j] = 0;
       for (int j = 0; j < B[i].size(); j ++) D[i][int(B[i][j] - 'A')] ++;
    }
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
       scanf("%s", A);
       for (int i = 0; i < 26; i++) C[i] = 0;
       for (int i = 0; i < strlen(A);  i++) {
          C[int(A[i] -'A')] ++;
       }
       string ret = "";
       for (int i = 0; i < 10; i++) {
          int k = order[i];
          int n = 102400;
          for (int j = 0; j < 26; j++) if (D[k][j] > 0) {
             if (C[j] / D[k][j] < n) {
               n = C[j] / D[k][j];
             }
          }
          for (int j = 0; j < B[k].size(); j++) {
             C[int(B[k][j]-'A')] -= n;
          }
          for (int j = 0; j < n; j++) {
            ret.push_back(char('0' + k));
          }
       }
       sort(ret.begin(), ret.end());
       printf("Case #%d: %s\n", t, ret.c_str());
    }
}
