#include <cstdio>

using namespace std;


int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t,k,i,j,c,n,c1,c2;
    scanf("%d",&t);

    char s[100][101];

    for(k=1;k<=t;k++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%s",&s[i]);

        i=j=1;
        c=0;

        if(s[0][0]!=s[1][0])
        {
            c=-1;
        }
        else
        {while(s[0][i]!='\0' || s[1][j]!='\0')
        {
          if(s[0][i]!=s[1][j])
          {
              if(s[0][i]==s[1][j-1])
              {
                  while(s[0][i]==s[1][j-1])
                  {
                      i++;
                      c++;
                  }
              }
              else if(s[0][i-1]==s[1][j])
              {
                  while(s[0][i-1]==s[1][j])
                  {
                      j++;
                      c++;
                  }
              }
              else
              {
                  c=-1;
                  break;
              }
          }
          else
          {
              i++;
              j++;
          }
        }}

        if(c==-1)
            printf("Case #%d: Fegla Won\n",k);
        else
            printf("Case #%d: %d\n",k,c);

    }

    return 0;
}
