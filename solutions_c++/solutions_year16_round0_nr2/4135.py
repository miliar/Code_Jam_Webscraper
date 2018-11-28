#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
bool arr[1004];
int len;
int res;
//void out();
bool check(){
  //printf("%d\n",res);
  for(int i=1;i<=len;i++){
    if(arr[i]==false){
      return false;
    }
  }
  return true;
}
// void out(){
//   for(int i=1;i<=len;i++){
//     if(arr[i]==true){
//       printf("+");
//     }else {
//       printf("-");
//     }
//   }
//   puts("");
// }
void execute(){
  int last = -1;
  for(int i=1;i<=len;i++){
    if(arr[i]!=arr[1]){
      last = i-1;
      break;
    }
  }
  if(last==-1){
    last = len;
  }
  for(int i=1;i<=last;i++){
    arr[i] = !arr[i];
  }
  res++;
}
char ch[1004];
int main(){
  int T;
  scanf("%d",&T);
  for(int cas=1;cas<=T;cas++){
    res=0;
    scanf("%s",&ch[1]);
    len = strlen(&ch[1]);
    for(int i=1;i<=len;i++){
      arr[i] = (ch[i] == '+' ? true: false);
    }
    while(check()== false){
      execute();
    }
    printf("Case #%d: ", cas);
    printf("%d\n", res);
  }
  return 0;
}