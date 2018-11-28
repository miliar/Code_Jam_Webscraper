#include <cstdio>
#include <cstring>

using namespace std;

const int MAXLEN = 100 + 2;

int T;
char S[MAXLEN];

int count(char s[]){
  bool fromLeft = true;

  int p = 0, q = strlen(s)-1;
  int ans = 0;

  while(p <= q){
    if(fromLeft){
      bool hasOp = false;
      if(s[p] == '+') hasOp = true;
      while(s[p] == '+' && p <= q) p++;
      if(p > q) break;
      if(hasOp) ans++;  // has '+', and now found '-'

      ans++;  // since s[p] == '-'
      while(s[p] == '-' && p <= q) p++;
      while(s[q] == '+' && p <= q) q--;

      //printf("Left:  p:%d q:%d ans:%d\n",p, q, ans);

      fromLeft = false;
    }
    else{
      bool hasOp = false;
      if(s[q] == '-') hasOp = true;
      while(s[q] == '-' && p <= q) q--;
      if(p > q) break;
      if(hasOp) ans++;  // has '-', now found '+'

      ans++; // since s[q] == '+'
      while(s[q] == '+' && p <= q) q--;
      while(s[p] == '-' && p <= q) p++;

      //printf("Right:  p:%d q:%d ans:%d\n",p, q, ans);

      fromLeft = true;
    }
  }

  return ans;
}


int main(){
  scanf("%d",&T);

  for(int i=0;i<T;i++){
    scanf(" %s", S);
    int ans = count(S);
    printf("Case #%d: %d\n", i+1, ans);
  }

  return 0;
}


