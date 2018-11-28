#include <iostream>
using namespace std;
struct sq {
  int h;
  bool hor;
  bool ver;
  sq() {
    h=0;
    hor=true;
    ver=true;
  }
};
int main() {
 int ntc;
 scanf("%d\n",&ntc);
 int hmax=100;
 sq lawn[101][101]={};
 int n,m;
 bool doable;
 for(int tc=1;tc<=ntc;++tc) {
   //read lawn
   scanf("%d %d\n",&n,&m);
   for(int i=1;i<=n;i++){
     lawn[i][0].h=0;
     lawn[i][0].hor=true;
     lawn[i][0].ver=true;
   }
   for(int i=1;i<=m;i++){
     lawn[0][i].h=0;
     lawn[0][i].hor=true;
     lawn[0][i].ver=true;
   }
   for(int i=1;i<=n;i++) {
     for(int j=1;j<=m-1;j++) {
       scanf("%d ",&lawn[i][j].h);
       lawn[i][j].hor=true; lawn[i][j].ver=true;
       if(lawn[i][j].h>lawn[i][0].h) lawn[i][0].h=lawn[i][j].h;
       if(lawn[i][j].h>lawn[0][j].h) lawn[0][j].h=lawn[i][j].h;
     }
     scanf("%d\n",&lawn[i][m].h);
     lawn[i][m].hor=true; lawn[i][m].ver=true;
     if(lawn[i][m].h>lawn[i][0].h) lawn[i][0].h=lawn[i][m].h;
     if(lawn[i][m].h>lawn[0][m].h) lawn[0][m].h=lawn[i][m].h;
   }
   doable=true;
   if(n>1 && m>1) {
     doable=true;
     // go through all lines
     for(int i=1;i<=n;i++) {
       for(int j=1;j<=m;j++) {
         if(lawn[i][j].h<lawn[i][0].h) lawn[i][j].hor=false;
       }
     }
     // go through all columns
     for(int i=1;i<=n;i++) {
       if(doable)
       for(int j=1;j<=m;j++) {
         if(lawn[i][j].h<lawn[0][j].h) {
           lawn[i][j].ver=false;
           if((!(lawn[i][j].hor)) && lawn[i][j].h!=hmax) {
             doable=false;
             break;
           }
         }
       }
     }
   }

   printf("Case #%d: ",tc);
   if(doable) printf("YES\n");
   else printf("NO\n");
 }
 return 0;
}
