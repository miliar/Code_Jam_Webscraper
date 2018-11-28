#include<iostream>
#include<cstring>
#include<string>
#include<cstdio>
#include<algorithm>
using namespace std;
long long base[18][18];
void pre(){
  for(long long t=2;t<=10;t++){
    base[t][0]=1;
    for(int s=1;s<18;s++){
      base[t][s] = base[t][s-1]* t;
    }
  }
}
long long getDiv(long long a){
  for(long long t = 2;t*t<=a;t++){
    if(a%t == 0){
      return t;
    }
  }
  return -1;
}
long long arr[12];
long long getBase(int num, int b){
  int ind = 0;
  long long res = 0;
  while(num){
    if(num%2){
      res+=base[b][ind];
    }
    ind++;
    num/=2;
  }
  return res;
}
char ch[20];
void getString(int a){
  int ind=0;
  while(a){
    if(a%2){
      ch[ind++]='1';
    } else {
      ch[ind++]='0';
    }
    a/=2;
  }
  reverse(ch,ch+ind);
  ch[ind]=0;
}
bool getDivs(int a){
  for(int i=2;i<=10;i++){
      arr[i]=getDiv(getBase(a,i));
      if(arr[i]==-1){
        return false;
      }
  }
  //printf("true");
  return true;
}
int main(){
  pre();
  int T,N,J;
  scanf("%d",&T);
  for(int cas=1;cas<=T;cas++){
    scanf("%d%d",&N,&J);
    int begin = 1 + (1<<(N-1));
    int up = 1<<N;
    //printf("%d %d", begin, up);
    int res = 0;
    printf("Case #%d:\n",cas);
    while(res<J&&begin<up){
      // printf("in looop");
      // getString(begin);
      // printf("test %s\n",ch);
      if(getDivs(begin)){
        getString(begin);
        printf("%s",ch);
        for(int i=2;i<=10;i++){
          printf(" %lld",arr[i]);
        }
        printf("\n");
        res++;
      }
      begin+=2;
    }
  }
  return 0;
}