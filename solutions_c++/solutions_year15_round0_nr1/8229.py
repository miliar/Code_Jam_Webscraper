#include <cstdio>

int main()
{ int t ; int n ; int x ;
  int ans ; char ch[1001] ; 
  scanf("%d",&t) ; 
  for(int ctr = 1 ; ctr<=t ; ctr++)
  { scanf("%d",&n) ; int cnt = 0 ; ans = 0 ;  
    scanf("%s",ch) ; 
    for(int ctr2 = 0 ;ch[ctr2]!='\0';ctr2++)
    { x = (int)ch[ctr2] - 48 ; 
      if(x)
      { if(cnt>=ctr2) { cnt+=x ; }
        else { ans+=ctr2-cnt ; cnt = ctr2+x ;    } } }
   printf("Case #%d: %d\n",ctr,ans) ; } return 0 ; }
