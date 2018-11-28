#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>
#define P printf
#define PN printf("\n");
#define PR(a) printf("%d",a);
#define PRN(a) printf("%d\n",a);

using namespace std;

#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define sqr(a) ((a)*(a))
#define FR(i,n) for (int i = 0; i < (n); i++)
#define DN(i,a) for(int i = (a)-1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define Set(a,c) memset(a, c, sizeof(a))
#define oo 1000000000
#define MAXN 100005
#define S(a) scanf("%d",&a);
#define SN(a) printf("%d\n",a);

int main ()
{
    //freopen("in.txt","rt",stdin);
    //freopen("hello.txt","wt",stdout);
	int i,j,t,n,m,x,y,no,save,r;
	char str[15][10]={"XXXX","XXXT","XXTX","XTXX","TXXX",
	               "OOOO","OOOT","OOTO","OTOO","TOOO"
	               };
  long k;
  char a[6][6],b[6][6],diag1[5],diag2[5];
  scanf("%d",&t);
  int test=0;
  //printf("t==%d\n",t);
  while(t--)
  {
      int no=0,f=0;
      test++;
      printf("Case #%d: ",test);

      for(i=0;i<4;i++){
            scanf("%s",a[i]);
            FOR(j,0,3)if(a[i][j]=='T'||a[i][j]=='X'||a[i][j]=='O')no++;
            FOR(j,0,3)if(j==i){diag1[j]=a[i][j];}
            FOR(j,0,3)if(j+i==3){diag2[j]=a[i][j];}
        //    puts(a[i]);
      }
      diag1[i]='\0';diag2[i]='\0';
FOR(i,0,3)
       FOR(j,0,3)
          b[j][i]=a[i][j];

for(i=0;i<4;i++)b[i][4]='\0';
      //puts(diag1);for(i=0;i<4;i++)printf("%c",diag2[i]);PN
      int won=-1;
     FOR(j,0,3)
     {
       FOR(k,0,9)
       {
       if(strcmp(a[j],str[k])==0)
       {
           if(k<=4)won=1;
           else won=2;
//printf("HTGFKJG\n");
           f==-1;break;
       }
       }
       if(f==-1)break;
     }
    FOR(j,0,3)
     {
       if(f==-1)break;
       //printf("ewqeqwjdfyghjlcgdjcv,jd\n");
       //puts(b[0]);
       FOR(k,0,9)
       {
       if(strcmp(b[j],str[k])==0)
       {
           if(k<=4)won=1;
           else won=2;
//printf("dbgghsdf\n");
           f==-1;break;
       }
       }

     }
     if(won==-1)
     {
      FOR(k,0,9)
       {if(strcmp(diag1,str[k])==0)
       {
         if(k<=4)won=1;
           else won=2;//;printf("........\n");

         break;
       }
       if(strcmp(diag2,str[k])==0)
       {
         if(k<=4)won=1;
           else won=2;//printf("+++++++++\n");
         break;
       }}
      }
if(won==-1&&no==16)
won=-2;
//printf("no=%d",no);
if(won==-2)printf("Draw\n");
else if(won==-1)printf("Game has not completed\n");
else if(won==1)printf("X won\n");
else if(won==2)printf("O won\n");
  }
 return 0;
}
