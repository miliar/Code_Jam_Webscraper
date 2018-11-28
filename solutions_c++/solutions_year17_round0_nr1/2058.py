#include <cstdio>
#include <cstring>

#define MAX_LEN 2000

char s[MAX_LEN];
int k;
int n;

void solve(int t)
{
  scanf("%s %d",s,&k);
  n = strlen(s);
  int c = 0;
  
  for(int i=0; i<n-k+1; i++) {
    if(s[i] == '-') {
      for(int j=0; j<k; j++) {
        s[i+j] = (s[i+j] == '+') ? '-' : '+';
      }
      c++;
    }
  }
  bool done = true;
  for(int i=n-k+1; i<n; i++) {
    if(s[i] == '-') {
      done = false;
    }
  }
  if(done) {
    printf("Case #%d: %d\n",t,c);
  } else {
    printf("Case #%d: IMPOSSIBLE\n",t);
  }
}



main()
{
  int t;
  scanf("%d",&t);
  for(int tt=0; tt<t; tt++) {
    solve(tt+1);
  }
}
