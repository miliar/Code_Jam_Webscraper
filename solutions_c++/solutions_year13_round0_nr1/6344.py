#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<cmath>
#include<queue>
#define mod 100000000
#define inf 1<<30
using namespace std;
char map[4][10];
int main(){
   // freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);

  int t;
  scanf("%d",&t);
  int x,y;
  for(int cas=1;cas<=t;++cas){
    getchar();
    int f=0;
    x=-1;
    y=-1;
    for(int i=0;i<4;++i){
      scanf("%s",map[i]);
     // printf("%s\n",map[i]);
     // getchar();
      for(int j=0;j<4;++j){
        if(map[i][j]=='.')f=1;
        if(map[i][j]=='T'){
          x=i;
          y=j;
        }
      }
    }
    int flag=0;
    if(x!=-1)
    map[x][y]='X';
    for(int i=0;i<4;++i){
      if(map[i][0]==map[i][1]&&map[i][0]==map[i][2]&&map[i][0]==map[i][3]){
        if(map[i][0]=='X'){
          flag=1;
          break;
        }else if(map[i][0]=='O'){
          flag=2;
          break;
        }
      }
    }
  //  cerr<<flag<<endl;
    if(x!=-1) map[x][y]='O';

    for(int i=0;i<4;++i){
      if(map[i][0]==map[i][1]&&map[i][0]==map[i][2]&&map[i][0]==map[i][3]){
        if(map[i][0]=='X'){
          flag=1;
          break;
        }else if(map[i][0]=='O'){
       //   cerr<<"i: "<<i<<endl;
          flag=2;
          break;
        }
      }
    }
    //cerr<<flag<<endl;
if(x!=-1)
     map[x][y]='X';
    for(int i=0;i<4;++i){
      if(map[0][i]==map[1][i]&&map[0][i]==map[2][i]&&map[0][i]==map[3][i]){
        if(map[0][i]=='X'){
          flag=1;
          break;
        }else if(map[0][i]=='O'){
          flag=2;
          break;
        }
      }
    }
    //cerr<<flag<<endl;
    if(x!=-1)
     map[x][y]='O';
    for(int i=0;i<4;++i){
      if(map[0][i]==map[1][i]&&map[0][i]==map[2][i]&&map[0][i]==map[3][i]){
        if(map[0][i]=='X'){
          flag=1;
          break;
        }else if(map[0][i]=='O'){
          flag=2;
          break;
        }
      }
    }
   // cerr<<flag<<endl;
     if(x!=-1)
     map[x][y]='X';
     if(map[0][0]==map[1][1]&&map[0][0]==map[2][2]&&map[0][0]==map[3][3]){
       // cerr<<"1:"<<flag<<endl;
        if(map[0][0]=='X'){
          flag=1;
         // break;
        }else if(map[0][0]=='O'){
          flag=2;
          //break;
        }
     }
  //  cerr<<"2:"<<flag<<endl;
    if(x!=-1)
     map[x][y]='O';
     if(map[0][0]==map[1][1]&&map[0][0]==map[2][2]&&map[0][0]==map[3][3]){
        if(map[0][0]=='X'){
          flag=1;
         // break;
        }else if(map[0][0]=='O'){
          flag=2;
        //  break;
        }
     }
    // cerr<<flag<<endl;
     if(x!=-1)
     map[x][y]='X';
     if(map[0][3]==map[1][2]&&map[0][3]==map[2][1]&&map[0][3]==map[3][0]){
        if(map[0][3]=='X'){
          flag=1;
         // break;
        }else if(map[0][3]=='O'){
          flag=2;
          //break;
        }
     }
    // cerr<<flag<<endl;
     if(x!=-1)map[x][y]='O';
    if(map[0][3]==map[1][2]&&map[0][3]==map[2][1]&&map[0][3]==map[3][0]){
        if(map[0][3]=='X'){
          flag=1;
          //break;
        }else if(map[0][3]=='O'){
          flag=2;
          //break;
        }
     }

    // cerr<<flag<<endl;
     printf("Case #%d: ",cas);
     if(flag==1){
       printf("X won\n");
     }else if(flag==2){
       printf("O won\n");
     }else{
       if(f==1){
         printf("Game has not completed\n");
       }else{
         printf("Draw\n");
       }
     }
    // getchar();
  }
  return 0;
}
