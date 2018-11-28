#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define L 101

int main(void) {
  /*
    T 100
      Number of test case
    N L
      Number of consective consonants
    L 
      10^2 for small case
      10^6 for large case
      Length of name
   */
  int t,tt,n,l;
  int c=0;
  char name[L];
  cin>>t;
  tt=t;
  while (t--) {
    memset(name,0,sizeof(name)*sizeof(char));
    c=0;
    printf("Case #%d: ",tt-t);
    scanf("%s",name);
    //puts(name);
    scanf("%d",&n);
    //printf("%d\n",n);
    char*v=(char*)malloc((n+1)*sizeof(char));
    for (int i=0;i<n;i++) v[i]='1';
    v[n]='\0';
    l=strlen(name);
    //printf("%d\n",l);
    for (int i=0;i<l;i++) {
      if (name[i]=='a' ||
          name[i]=='e' ||
          name[i]=='i' ||
          name[i]=='o' ||
          name[i]=='u') name[i]='0';
      else name[i]='1';
    }
    for (int i=0;i<l;i++) {
      for (int j=i+n;j<=l;j++) {
        for (int k=i;k+n<=j;k++) {
          if (!strncmp(name+k,v,n)) {
            /*
            for (int x=i;x<j;x++)
              putchar(name[x]);
            puts("");
            */
            c++;
            break;
          }
        }
      }
    }
    //printf("%s %d\n",name,n);
    printf("%d\n",c);
    free(v);
  }
  return 0;
}
