#include <iostream> 
#include <sstream> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <memory> 
#include <cctype> 
#include <string> 
#include <vector>
#include <map> 
#include <set> 
#include <algorithm> 
#include <cstring>
using namespace std;
char str[10][10];
int dx[]={-1,0,1,1};
int dy[]={1,1,1,0};
int main()
{
    int t,i,j,s,p,q,l,cnt,nx,ny,tst=0;
    bool over;
    freopen("debug\\input.txt","r",stdin);
    freopen("debug\\output.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
          tst++;
          for(i=0;i<4;i++) 
             scanf("%s",str[i]);
          over=true;
          printf("Case #%d: ",tst);
          for(i=0;i<4;i++)
          {
            for(j=0;j<4;j++)
            {
                 if(str[i][j]=='.')
                 {
                     over=false;
                     continue;
                 }
                 for(s=0;s<4;s++)
                 {
                     cnt=1;
                     for(l=1;;l++)
                     {
                          nx=i+l*dx[s];
                          ny=j+l*dy[s];
                          if(nx>=0&&nx<4&&ny>=0&&ny<4&&(str[nx][ny]==str[i][j]||str[nx][ny]=='T'))
                              cnt++;
                          else
                              break;
                     }
                     for(l=1;;l++)
                     {
                          nx=i-l*dx[s];
                          ny=j-l*dy[s];
                          if(nx>=0&&nx<4&&ny>=0&&ny<4&&(str[nx][ny]==str[i][j]||str[nx][ny]=='T'))
                               cnt++;
                          else
                              break;
                     }
                     if(cnt>=4)
                         break;
                 }
                 if(s<4)
                    break;
            }
            if(j<4)
               break;
          }
          if(i<4)
             printf("%c won\n",str[i][j]);
          else
          {
              if(over) 
                 printf("Draw\n");
              else
                 printf("Game has not completed\n");
          }
    }
    return 0;
}
