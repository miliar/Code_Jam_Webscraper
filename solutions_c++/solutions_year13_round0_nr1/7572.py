#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<math.h>
#include <iomanip>
using namespace std;
int n,i,k,sum,d,f,j,m,ans,r,t,y,x,u,N,I;
string a[6];
void gtx(){ ans=0;
     for (u=0; u<4; u++){
         if ((a[u][0]=='X' || a[u][0]=='T') && (a[u][1]=='X' || a[u][1]=='T') && (a[u][2]=='X' || a[u][2]=='T') && (a[u][3]=='X' || a[u][3]=='T')) ans=1;
         }
         if (ans==1) return;// cout<<a[0][2]<<" ";
        
         for (u=0; u<4; u++){
         if ((a[0][u]=='X' || a[0][u]=='T') && (a[1][u]=='X' || a[1][u]=='T') && (a[2][u]=='X' || a[2][u]=='T') && (a[3][u]=='X' || a[3][u]=='T')) ans=1;
         }
      if (ans==1) return;
     
     if ((a[0][0]=='X' || a[0][0]=='T') && (a[1][1]=='X' || a[1][1]=='T') && (a[2][2]=='X' || a[2][2]=='T') && (a[3][3]=='X' || a[3][3]=='T')) ans=1;
     
     if (ans==1) return;
     
     if ((a[0][3]=='X' || a[0][3]=='T') && (a[1][2]=='X' || a[1][2]=='T') && (a[2][1]=='X' || a[2][1]=='T') && (a[3][0]=='X' || a[3][0]=='T')) ans=1;
     
return;
     }
     
void gto(){ ans=0;
     for (u=0; u<4; u++){
         if ((a[u][0]=='O' || a[u][0]=='T') && (a[u][1]=='O' || a[u][1]=='T') && (a[u][2]=='O' || a[u][2]=='T') && (a[u][3]=='O' || a[u][3]=='T')) ans=1;
         }
         if (ans==1) return;
         
         for (u=0; u<4; u++){
         if ((a[0][u]=='O' || a[0][u]=='T') && (a[1][u]=='O' || a[1][u]=='T') && (a[2][u]=='O' || a[2][u]=='T') && (a[3][u]=='O' || a[3][u]=='T')) ans=1;
         }
      if (ans==1) return;
     
     if ((a[0][0]=='O' || a[0][0]=='T') && (a[1][1]=='O' || a[1][1]=='T') && (a[2][2]=='O' || a[2][2]=='T') && (a[3][3]=='O' || a[3][3]=='T')) ans=1;
     
     if (ans==1) return;
     
     if ((a[0][3]=='O' || a[0][3]=='T') && (a[1][2]=='O' || a[1][2]=='T') && (a[2][1]=='O' || a[2][1]=='T') && (a[3][0]=='O' || a[3][0]=='T')) ans=1;
     
return;
     }
main(){
      //freopen("a.in","r",stdin);
     // freopen("a.out","w",stdout);
      
      scanf("%d",&N);
      
      for (I=1; I<=N; I++){ d=0;
          for (i=0; i<4; i++){ cin>>a[i]; for (j=0; j<4; j++) if (a[i][j]!='.') d++;}
         
         
        gtx();
          if (ans==1) cout<<"Case #"<<I<<": "<<"X won";
          else {gto();
          if (ans==1) cout<<"Case #"<<I<<": "<<"O won";
          else if (d==16) cout<<"Case #"<<I<<": "<<"Draw";
          else cout<<"Case #"<<I<<": "<<"Game has not completed";}
          cout<<endl;
          }
          
}
