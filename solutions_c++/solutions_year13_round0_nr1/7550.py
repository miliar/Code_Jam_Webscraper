#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
char s[5][5];
bool emp;
inline void find_T()
{
       for (int i=0;i<4;i++)
           for (int j=0;j<4;j++)
               if (s[i][j]=='.')
               {
                  emp=true;
                  return;
               }
}
inline bool check(int x,int y,char ch)
{
       return (s[x][y]==ch||s[x][y]=='T');
}
inline int calc(char ch)
{
       if (check(0,0,ch)&&check(1,1,ch)&&check(2,2,ch)&&check(3,3,ch)) return 1;
       if (check(3,0,ch)&&check(2,1,ch)&&check(1,2,ch)&&check(0,3,ch)) return 1;
       for (int i=0;i<4;i++)
           if (check(i,0,ch)&&check(i,1,ch)&&check(i,2,ch)&&check(i,3,ch)) return 1;
       for (int i=0;i<4;i++)
           if (check(0,i,ch)&&check(1,i,ch)&&check(2,i,ch)&&check(3,i,ch)) return 1;
       if (emp) return -1;
       else return 0;
}
int main(int argc, char *argv[])
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int dex=1;dex<=t;dex++)
    {
        for (int i=0;i<4;i++)
            scanf("%s",s[i]);
        emp=false;
        find_T();
        int ax=calc('X');
        int bx=calc('O');
        if (ax>=0&&ax==bx) printf("Case #%d: Draw\n",dex);
        else if (ax>0) printf("Case #%d: X won\n",dex);
        else if (bx>0) printf("Case #%d: O won\n",dex);
        else printf("Case #%d: Game has not completed\n",dex);
    }
  //  system("PAUSE");
    return EXIT_SUCCESS;
}
