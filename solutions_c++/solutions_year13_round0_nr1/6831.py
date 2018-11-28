#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<cstdlib>
#include<stack>
#include<queue>
#include<string>
#include<cstring>
#include<set>
#include<map>
#include<utility>

#define PR(x) cout<<#x<<"="<<x<<endl
#define READ2(x,y) scanf("%d %d",&x,&y)
#define REP(i,a) for(int i=0;i<a;i++)
#define READ(x) cin>>x
#define PRARR(x,n) for(int i=0;i<n;i++)printf(#x"[%d]=\t%d\n",i,x[i])
#define rd(arr,i,n) for(int i=0;i<n;i++) cin>>arr[i]
#define PB push_back
#define SUM(arr,n,sum) {sum=0;for(int i=0;i<n;i++) sum+=arr[i]; }
#define VC vector
#define CLR(arr) memset(arr,0,sizeof(arr))
#define FILL(arr,val) memset(arr,val,sizeof(arr))
using namespace std;
char matr[6][6];
bool checkcomplete(){
  REP(i,4) REP(j,4) if(matr[i][j]=='.') return false;
  return true;
}
void PRINT(){
 // REP(i,4) puts(matr[i]);
}
bool __check(char turn){
  int psx=-1,psy=-1;
  REP(i,4) REP(j,4){
    if(matr[i][j]=='T'){
      psx=i;psy=j;
      matr[i][j]=turn;
      break;
    }
  if(psx!=-1) break;
  }
  int i=0;
  REP(j,4)
    if(matr[i][j]==turn&&matr[i][j]==matr[i+1][j]&&matr[i+1][j]==matr[i+2][j]&&matr[i+2][j]==matr[i+3][j]){
      if(psx!=-1)matr[psx][psy]='T';
      return true;
    }
 REP(j,4)
    if(matr[j][i]==turn&&matr[j][i]==matr[j][i+1]&&matr[j][i+1]==matr[j][i+2]&&matr[j][i+2]==matr[j][i+3]){
      if(psx!=-1)matr[psx][psy]='T';
      return true;
    }
 int j=0;i=0;   
 if(matr[i][j]==turn&&matr[j][i]==matr[j+1][i+1]&&matr[j+1][i+1]==matr[j+2][i+2]&&matr[j+2][i+2]==matr[j+3][i+3]){
      if(psx!=-1)matr[psx][psy]='T';
      return true;
    }
  i=3;j=0;  
  if(matr[j][i]==turn&&matr[j][i]==matr[j+1][i-1]&&matr[j+1][i-1]==matr[j+2][i-2]&&matr[j+2][i-2]==matr[j+3][i-3]){
      if(psx!=-1)matr[psx][psy]='T';
      return true;
    }
  if(psx!=-1) matr[psx][psy]='T';  
  return false;   
}
int check(){
  if(__check('X')) return 2;
  PRINT();
  if(__check('O')) return 3;
  PRINT();
  if(checkcomplete()) return 1;
  PRINT();
  return 0; 
}
int main(){
  int t;
  scanf("%d",&t);
  for(int x=1;x<=t;x++){
    printf("Case #%d: ",x);
    REP(i,4){
      scanf("%s",matr[i]);
    }
  switch(check()){
    case 0: puts("Game has not completed");break;
    case 1: puts("Draw");break;
    case 2: puts("X won");break;
    case 3: puts("O won");break;
  }
  }
}
