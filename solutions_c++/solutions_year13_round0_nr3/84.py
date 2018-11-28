#include <stdio.h>
#include <string.h>

int N;
char to[110], from[110];
int len;

int jum=0;
char DP[42000][110];
char kal[110];
int icase;

void flipper(){
  len = N*2;
  for(int i=0; i<N; i++){
    from[len-i-1] = from[i];
  }
}

void flipper2(){
  len = N*2-1;
  for(int i=0; i<N; i++){
    from[len-i-1] = from[i];
  }
}

bool test(){
  for(int i=0; i<110; i++) to[i] = 0;
  
  for(int i=0; i<len; i++){
    for(int j=0; j<len; j++){
      to[i+j] += from[i]*from[j];
      if(to[i+j] >= 10) return false;
    }
  }
  
  //for(int i=0; i<len; i++) printf("%c", from[i]+48);
  //printf("\n");
  int nlen = len*2-1;
  for(int i=0; i<nlen; i++) DP[jum][101-nlen+i] = to[i]+'0';
  for(int i=0; i<101-nlen; i++) DP[jum][i] = '0';
  DP[jum][101] = '\0';
  
  jum++;
  return true;
}

void rec(int level){
  if (level >= N){
    return;
  }
  
  if(level > 0) rec(level+1);
  for(int i=1; i<=2; i++){
    from[level] = i;
    flipper();
    if(!test()){
      from[level] = 0;
      return;
    }
    rec(level+1);
  }
  from[level] = 0;
}

void rec2(int level){
  if (level >= N){
    return;
  }
  
  int end = 2;
  if(level > 0) rec2(level+1);
  if(N == 1) end = 3;
  
  for(int i=1; i<=end; i++){
    from[level] = i;
    flipper2();
    if(!test()){
      from[level] = 0;
      return;
    }
    rec2(level+1);
  }
  from[level] = 0;
}

int binsearch(bool &got){
  int lo = 0, hi = jum-1, mid;
  int res;
  int ret=0;
  
  while(lo <= hi){
    mid = (lo+hi)/2;
    
    res = strcmp(kal, DP[mid]);
    if(res >= 0){
      lo = mid+1;
      ret = mid;
      if(res == 0) got = true;
    }
    else if(res < 0)hi = mid-1;
  }
  
  return ret;
}

void Parse(char *str){
  int l = strlen(str);
  
  for(int i=l-1; i>=0; i--) str[100+i-(l-1)] = str[i];
  str[101] = '\0';
  for(int i=0; i<100-(l-1); i++) str[i] = '0';
  //puts(str);
}

int main(){
  int lim = 25;
  int jcase;
  int v1, v2;
  bool got;
  
  for(int i=0; i<lim; i++) from[i] = 0;
  
  for(int i=0; i<lim; i++){
    for(int j=0; j<lim; j++) from[j] = 0;
    N = i+1;
    rec2(0);
    rec(0);
  }
  
  freopen("C-large-2.in", "r", stdin);
  freopen("C-large-2.out", "w", stdout);
  
  scanf("%d", &jcase);
  for(icase=0; icase<jcase; icase++){
    scanf("%s", kal);
    Parse(kal);
    got = false;
    v1 = binsearch(got);
    if(got) v1--;
    
    scanf("%s", kal);
    Parse(kal);
    got = false;
    v2 = binsearch(got);
    
    printf("Case #%d: %d\n", icase+1, v2-v1);
  }
  return 0;
}
