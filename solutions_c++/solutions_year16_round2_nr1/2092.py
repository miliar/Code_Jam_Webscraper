#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<ctime>
using namespace std;
string tt[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
char ch[10] = {'Z','U','W','O','R','T','F','X','I','V'};
int num[10] = {0,   4,  2,  1,  3,  8,  5,  6,  9,  7};
char res[3000];
int ct[400],total[10];
int main(){
  int T;
  scanf("%d",&T);
  for(int cas=1;cas<=T;cas++){
    scanf("%s",res);
    int len = strlen(res);
    memset(ct,0,sizeof(ct));
    memset(total,0,sizeof(total));
    for(int i=0;i<len;i++){
      ct[res[i]]++;
    }
    for(int i=0;i<10;i++){
      total[num[i]]=ct[ch[i]];
      for(int j=0;j<tt[num[i]].length();j++){
        ct[tt[num[i]][j]] -= total[num[i]];
      }
    }
    printf("Case #%d: ",cas);
    for(int i=0;i<10;i++){
      while(total[i]--){
        printf("%d",i);
      }
    }
    printf("\n");
  }
  return 0;
}