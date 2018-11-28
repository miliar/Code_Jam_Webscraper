#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

char tab[50][50];



bool solve(int r, int c, int m){
//printf("%d %d %d\n",r,c,m);
  if(!m)return true; //no mine


  if(r*c==m+1){//all-but-one
        for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
          tab[i][j]='*';
        }}    
    return true;
  }

  if((r==2 || c==2)&& m+2==r*c ){//all but two
    return false;
  }
  
  if(r==2){//2rows
//printf("r2 %d %d %d\n",r,c,m);
    if(m%2)return false;

    for(int i=c-m/2;i<c;i++){
      tab[0][i]='*';
      tab[1][i]='*';
    }
  }

  if(c==2){//2 cols
    if(m%2)return false;
//printf("c2 %d %d %d\n",r,c,m);

    for(int i=r-m/2;i<r;i++){
      tab[i][0]='*';
      tab[i][1]='*';
    }
    return true;
  }

  if(r==3 && c==3 && m==1){//3,3,1
    tab[2][2]='*';
    return true;
  }

  if(r==3 && c==3 && m==2){//3,3,2
    return false;
  }






// diminish max(r,c)  
  if(m>=r && r<=c){
//    printf("cas1\n");
        for(int i=0;i<r;i++){
          tab[i][c-1]='*';
        }
        return solve(r,c-1,m-r);
  }
  if(m>=c && c<=r){
//    printf("cas2\n");
        for(int i=0;i<c;i++){
          tab[r-1][i]='*';
        }
        return solve(r-1,c,m-c);
  }

//>3r, >3c, m<r,c
if(c-m>1){//1 line
for(int i=0;i<m;i++){tab[r-1][c-1-i]='*';}  
return true;}
else{
  //2 lines
for(int i=0;i<m-1;i++){tab[r-1][c-1-i]='*';}
tab[r-2][c-1]='*';
return true;}

return 1/0;
}






int main(){
  int ncases;
  scanf("%d",&ncases);
  int r,c,m;
  for(int cas=1;cas<=ncases;cas++){
    printf("Case #%d:\n",cas);
    scanf("%d %d %d",&r,&c,&m);
    int mi=min(r,c);

      int debut=1;
      int cases=r*c;
    if(mi==1){
      for(int i=0;i<r;i++){
      for(int j=0;j<c;j++){
        if(debut){printf("c");debut=0;m++;}else if(cases>m){m++;printf(".");}else{printf("*");}
      }
      printf("\n");
      }
      continue;
    }
    for(int i=0;i<r;i++)
    for(int j=0;j<c;j++)
      tab[i][j]='.';
    bool s=solve(r,c,m);
    tab[0][0]='c';
    if(!s)printf("Impossible\n");
    else
      for(int i=0;i<r;i++){
      for(int j=0;j<c;j++)
        printf("%c",tab[i][j]);
      printf("\n");
      }




    
    
    
  }
}
