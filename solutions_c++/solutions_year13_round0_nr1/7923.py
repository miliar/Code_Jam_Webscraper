#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<fstream>
#include<iostream>
#include<map>
#include<vector>
using namespace std;

int main() {
    freopen("A.in","rt",stdin);
    freopen("A.out","wt",stdout);
    int t,i,j,c,kc,wr;
    char g[4][4],k;
    bool win,d;
    scanf("%d",&t);
    for(c=0;c<t;++c) {
                     for(i=0;i<4;++i) for(j=0;j<4;++j) cin>>g[i][j];
                     printf("Case #%d: ",c+1);
                     for(i=0;i<4;++i) {
                                      win=true;
                                      k=g[i][0];
                                      if(k=='T') k=g[i][1];
                                      if(k=='.') {
                                                 win=false;
                                                 continue;
                                      }
                                      
                                      for(j=0;j<4;++j) {
                                                       if(g[i][j]!=k && g[i][j]!='T') {
                                                                       win=false;
                                                                       break;
                                                       }
                                      }
                                      if(win) break;
                     }
                     if(!win) {
                              for(i=0;i<4;++i) {
                                      win=true;
                                      k=g[0][i];
                                      if(k=='T') k=g[1][i];
                                      if(k=='.') {
                                                 win=false;
                                                 break;
                                      }
                                      for(j=0;j<4;++j) {
                                                       if(g[j][i]!=k && g[j][i]!='T') {
                                                                       win=false;
                                                                       break;
                                                       }
                                      }
                                      if(win) break;
                              }
                     }
                     if(!win) {
                              win=true;
                              k=g[0][0];
                              if(k=='T') k=g[1][1];
                              if(k=='.') win=false;
                              else {
                              for(i=0;i<4;++i) {
                                               if(g[i][i]!=k && g[i][i]!='T') {
                                                                              win=false;
                                                                              break;
                                               }
                              }
                              }
                              if(!win) {
                                       win=true;
                                       k=g[0][3];
                                       if(k=='T') k=g[1][2];
                                       if(k=='.') win=false;
                                       else {
                                       for(i=0;i<4;++i) {
                                                        if(g[i][3-i]!=k && g[i][3-i]!='T') {
                                                                                           win=false;
                                                                                           break;
                                                        }
                                       }
                                       }
                              }
                     }
                     if(win) {
                             if(k=='X') printf("X won\n");
                             else printf("O won\n");
                     }
                     else {
                          d=1;
                          for(i=0;i<4;++i) {
                                           for(j=0;j<4;++j) {
                                                            if(g[i][j]=='.') {
                                                                             d=0;
                                                                             break;
                                                            }
                                           }
                                           if(!d) break;
                          }
                          if(i==4 && j==4) printf("Draw\n");
                          else printf("Game has not completed\n");
                     }
    }
    //system("pause");
}
