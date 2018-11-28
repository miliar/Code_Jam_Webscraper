#include <iostream>
#include<cstdio>
#include<cstring>
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

void solve()
{
    char str[16],last[16];
    scanf("%s",str);
    int s=strlen(str);
    int cur=1,i,j;
    last[0]=str[0];
    for(i=1;i<s;i++)
    {
        if(last[0]>str[i])
        {
            last[cur++]=str[i];
        }
        else
        {
            for(j=cur;j>=0;j--)
            {
                last[j+1]=last[j];
            }
            last[0]=str[i];
            cur++;
        }
    }
    last[cur]='\0';
    printf("%s\n",last);
}
int main() {
  int tn;
  scanf("%d", &tn);
  forn(t, tn) {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}


