// next_permutation example
#include <iostream>     // std::cout
#include <algorithm>    // std::next_permutation, std::sort
using namespace std;
int main () 
{
     freopen("bin1.in","r",stdin);
     freopen("outp1.in","w",stdout);
    int t,t1;
    scanf("%d",&t);
    t1=t;
    while(t--)
    {
    int n;
    scanf("%d",&n);
    int myints[n];
    int i;
    for(i=0;i<n;i++)
           myints[i]=i;
  
  char s[n][101];
  for(i=0;i<n;i++)
  scanf("%s",s[i]);
  
 // int len;
 // for(i=0;i<n;i++)
 // len+=strlen(s[i]);
//printf("%d\n",len);
  int ans=0;
 
  do {
      char news[1002];
      strcpy(news,s[myints[0]]);
      for(i=1;i<n;i++)
      {

                      strcat(news,s[myints[i]]);
      }
    // printf("%s\n",news);
      int len = strlen(news);
      int a[26]={0};
      a[news[0]-'a']++;
      for(i=1;i<len;i++)
      {
             if(a[news[i]-'a']>0 && news[i]!=news[i-1])
             break;
             
             a[news[i]-'a']++;
                     
      }
     // printf("%d",i);
      if(i==len)
      ans++;
    
  } while ( next_permutation(myints,myints+n) );

   printf("Case #%d: %d\n",t1-t,ans);
}
  return 0;
}
