#include <iostream>
using namespace std;
int main()
{
    freopen("A-small-attempt3.in","r",stdin);
    freopen("A-small-attempt3.out","w",stdout);
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=0;i<T;i++){
             printf("Case #%d: ",i+1);
             char A[4][4];
             for(int j=0;j<4;j++)
                  scanf("%s",&A[j]);
             int X,O,D,N;
             for(int j=0;j<4;j++){
                  X=1;
                  for(int k=0;k<4;k++){
                      if(!((A[j][k]=='X')||(A[j][k]=='T'))){
                                  X=0;
                                  break;
                      }
                  }
                  if(X==1){
                      printf("X won\n");
                      break;
                  }
             }
             if(X==1)
                 continue;
             for(int j=0;j<4;j++){
                  X=1;
                  for(int k=0;k<4;k++){
                      if(!((A[k][j]=='X')||(A[k][j]=='T'))){
                                  X=0;
                                  break;
                      }
                  }
                  if(X==1){
                      printf("X won\n");
                      break;
                  }
             }
             if(X==1)
                  continue;
             X=1;
             for(int j=0,k=0;j<4,k<4;j++,k++){
                           if(!((A[j][k]=='X')||(A[j][k]=='T'))){
                                  X=0;
                                  break;
                            }
             }
             if(X==1)
                  printf("X won\n");
             if(X==1)
                  continue;
             X=1;
             for(int j=0,k=3;j<4,k>=0;j++,k--){
                           if(!((A[j][k]=='X')||(A[j][k]=='T'))){//if((j==1)&&(k==2))printf("FAULT");
                                  X=0;
                                  break;
                            }
             }
             if(X==1)
                 printf("X won\n");
             for(int j=0;j<4;j++){
                  O=1;
                  for(int k=0;k<4;k++){
                      if(!((A[j][k]=='O')||(A[j][k]=='T'))){
                                  O=0;
                                  break;
                      }
                  }
                  if(O==1){
                      printf("O won\n");
                      break;
                  }
             }
             if(O==1)
                 continue;
             for(int j=0;j<4;j++){
                  O=1;
                  for(int k=0;k<4;k++){
                      if(!((A[k][j]=='O')||(A[k][j]=='T'))){
                                  O=0;
                                  break;
                      }
                  }
                  if(O==1){
                      printf("O won\n");
                      break;
                  }
             }
             if(O==1)
                  continue;
             O=1;
             for(int j=0,k=0;j<4,k<4;j++,k++){
                           if(!((A[j][k]=='O')||(A[j][k]=='T'))){
                                  O=0;
                                  break;
                            }
             }
             if(O==1)
                  printf("O won\n");
             if(O==1)
                  continue;
             O=1;
             for(int j=0,k=3;j<4,k>=0;j++,k--){
                           if(!((A[j][k]=='O')||(A[j][k]=='T'))){//if((j==1)&&(k==2))printf("FAULT");
                                  O=0;
                                  break;
                            }
             }
             if(O==1)
                 printf("O won\n");
             if(O==1)
                  continue;
             D=0;
             for(int j=0;j<4;j++)
                  for(int k=0;k<4;k++)
                       if(A[j][k]=='.')
                            D=1;
             if(D==0)
                printf("Draw\n");
             else
                printf("Game has not completed\n");
             char c;
             scanf("%c",&c);
             if(c=='\n')
                  continue;
    }
    return 0;
}
