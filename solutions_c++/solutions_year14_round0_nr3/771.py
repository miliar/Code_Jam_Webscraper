#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int mat[55][55];
char ans[55][55];
bool unCovered[55][55];
int r,c,m,nm,sq;
int lastx,lasty,lastop;
int dx[]={1,0,-1},dy[]={1,0,-1};
void fill(){
  for(int i=1;i<55;i++)
    for(int k=1;k<55;k++){
      ans[i][k]='*';
      mat[i][k]=9;
      unCovered[i][k]=false;
    }
}
void printAns(){
  cout<<endl;
  if(ans[r][c]=='.')ans[r][c]='c';
  for(int i=1;i<=r;i++){
    for(int k=1;k<=c;k++){
      cout<<ans[i][k];
    }
    cout<<endl;
  }
}
void printMat(){
  ans[r][c]='c';
  for(int i=1;i<=r;i++){
    for(int k=1;k<=c;k++){
      cout<<mat[i][k];
    }
    cout<<endl;
  }
}
bool isValid(int x,int y){
  return x<=r&&x>=1&&y<=c&&y>=1;
}
int countAdjMines(int x,int y){
  int ret=0;
  for(int i=0;i<3;i++){
    for(int k=0;k<3;k++){
      if(dx[i]==0&&dy[k]==0)continue;
      if(!isValid(x+dx[i],y+dy[k]))continue;
      ret+=ans[x+dx[i]][y+dy[k]]=='*';
    }
  }
  return ret;
}
void uncover(int x,int y){
  if(!isValid(x,y)||unCovered[x][y])return;
  mat[x][y]=countAdjMines(x,y);
  unCovered[x][y]=true;
  if(mat[x][y]!=0) return;
  for(int i=0;i<3;i++){
    for(int k=0;k<3;k++){
      if(dx[i]==0&&dy[k]==0)continue;
      int nx=x+dx[i];
      int ny=y+dy[k];
      uncover(nx,ny);
    }
  }
}
bool verify(){
  uncover(r,c);
  for(int i=1;i<=r;i++){
    for(int k=1;k<=c;k++){
      if((ans[i][k]=='.')&&(mat[i][k]>8)){
        return false;
      }
    }
  }
  return true;
}
int findFirstRow(int row){
  if(!(row>=1&&row<=r)) return -1;
  for(int i=1;i<=c;i++){
    if(ans[row][i]=='.') return i;
  }
}
int findFirstCol(int col){
  if(!col>=1&&col<=r) return -1;
  for(int i=1;i<=r;i++){
    if(ans[i][col]=='.') return i;
  }
}
void doMagic(){
  if(lastx==-1)return;
  //cout<<"=== " <<lastx<<"  "<<lasty<<endl;
  if(lastop==1){
    int row=findFirstCol(lasty+1),col=lasty+1;
    if(!isValid(lastx-1,lasty)||!isValid(row,col))return;
    if(ans[row][col]=='*'||(row==r&&col==c))return;
    //cout<<row<<"  op1   "<<col<<"  "<<lastx-1<<"  "<<lasty<<endl;
    ans[row][col]='*';
    ans[lastx-1][lasty]='.';
  }else{
    int row=lastx+1,col=findFirstRow(lastx+1);
    if(!isValid(row,col)||!isValid(lastx,lasty-1))return;
    if(ans[row][col]=='*'||(row==r&&col==c))return;
    //cout<<row<<"   op2  "<<col<<"  "<<lastx-1<<"  "<<lasty<<endl;
    ans[row][col]='*';
    ans[lastx][lasty-1]='.';
  }
}
void clearUncovered(){
  for(int i=1;i<=r;i++)for(int k=1;k<=c;k++){
    unCovered[i][k]=false;
    mat[i][k]=9;
  }
}
int main(){
  int tc;
  scanf("%d",&tc);
  for(int tcc=1;tcc<=tc;tcc++){
    printf("Case #%d: ",tcc);
    scanf("%d %d %d",&r,&c,&m);
    fill();
    lastx=lasty=lastop=-1;
    nm=r*c-m;
    sq=sqrt(nm);
    if(sq>min(r,c)){
      sq=min(r,c);
    }
    int rem=nm-sq*sq;
    //cout<<sq<<"  "<<rem<<endl;
    for(int i=r-sq+1;i<=r;i++){
      for(int k=c-sq+1;k<=c;k++){
        ans[i][k]='.';
      }
    }
    //Gif we have one extra row and col empty
    if(r>=sq+1&&c>=sq+1){
      //cout<<"case1 and "<<rem<<endl;
      //fill sq elements in col
      int col=c-sq;
      int row=r;
      while((row>(r-sq))&&rem>0){
        ans[row][col]='.';
        //cout<<"placed at "<<row<<"  "<<col<<endl;
        //printAns();
        lastx=row; lasty=col;
        lastop=1;
        row--;
        rem--;
      }
      //cout<<rem<<endl;
      //fill rem in the row from right to left
      row=r-sq;
      col=c;
      while(rem>0){
        ans[row][col]='.';
        //cout<<"placed aa at"<<row<<"  "<<col<<"  "<<rem-1<<endl;
        //printAns();
        lastx=row; lasty=col; lastop=2;
        col--;
        rem--;
      }
    } else if(r>=sq+1){
      //col is filled, fill row wise right to left
      int row=r-sq,col=c;
      //cout<<"type 1\n";
      while(rem>0){
        ans[row][col]='.';
        lastx=row; lasty=col; lastop=2;
        rem--;
        col--;
        if(col==0){
          row--;
          col=c;
        }
      }
    } else {
      //row is filled , fill col bottom to top
      //cout<<"type 3\n";
      int row=r,col=c-sq;
      while(rem>0){
        ans[row][col]='.';
        lastx=row; lasty=col; lastop=1;
        rem--;
        row--;
        if(row==0){
          row=r;
          col--;
        }
      }
    }
    if(!verify()){
     //printAns();
     //printMat();
     doMagic();
      clearUncovered();
      if(verify()){
        //cout<<"magixxx\n";
        printAns();
        //printMat();
      } else {
        cout<<"\nImpossible\n";
        //printAns();
        //printMat();
      }
    }else{
      printAns();
      //printMat();
    }
  }
  return 0;
}
