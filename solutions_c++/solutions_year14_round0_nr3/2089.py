#include<iostream>
#include<cstring>
#include<stdio.h>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define F first
#define Se second
#define ll long long
#define INF 2000000000
using namespace std;
int T,t,n,m,P,i,j,O,cur,bu;
int a[7][7],b[7][7],f[7][7];
bool ele;


void pp(int x,int y){
     int i,j;
     
     for(i=-1;i<2;i++)
      for(j=-1;j<2;j++)
      if(x+i>0 && y+j>0 &&
         x+i<=n && y+j<=m && 
         !f[x+i][y+j]){
        f[x+i][y+j]=1;
        bu++;
        if(!b[x+i][y+j])pp(x+i,y+j);
      }          
}

void check(){
     int i,j,x=-1,y,k,e;
/*
    for(i=1;i<=n;i++){
     for(j=1;j<=m;j++)cout<<a[i][j]<<' ';
     cout<<endl;
     }
     system("pause");*/
     
     for(i=1;i<=n;i++)
       for(j=1;j<=m;j++){
         b[i][j]=0;
         for(k=-1;k<2;k++)
         for(e=-1;e<2;e++)
           if(a[i+k][j+e])b[i][j]++;
         
         if(x==-1 && b[i][j]==0)x=i,y=j;
       }//cout<<x<<' '<<y<<endl;
     if(x==-1)return;
     
     for(i=1;i<=n;i++)
      for(j=1;j<=m;j++)f[i][j]=0;
     bu=f[x][y]=1;
     pp(x,y);
     //cout<<bu<<' '<<O<<endl;
     if(bu==O)a[x][y]=3,ele=1;
}

void go(int x,int y){
     if(x>n){
        if(cur==O)
        check();
        return ;     
     }
     int nx=x,ny=y+1;
     if(ny>m)ny=1,nx++;
     
     if(cur<O){
         cur++;
         go(nx,ny);
         if(ele)return;
         cur--;
         }
    
     a[x][y]=1;
     go(nx,ny);
     if(ele)return;
     a[x][y]=0;
}


main()
{//freopen("C-small-attempt0.in","r",stdin);
freopen("C-small-attempt1.in","r",stdin); 
 freopen("output.txt","w",stdout);
 scanf("%d",&T);
 for(t=1;t<=T;t++){
     scanf("%d%d%d",&n,&m,&P);
     O=n*m-P;
     
     
     ele=cur=0;
     if(O!=1)
     go(1,1);
     printf("Case #%d:\n",t);
     
     if(O==1){
         for(i=1;i<=n;i++){
          for(j=1;j<=m;j++)
            if(i==1 && j==1)printf("c");else printf("*");
          printf("\n"); 
          }
     }else
     if(!ele)printf("Impossible\n");else{
        for(i=1;i<=n;i++){
          for(j=1;j<=m;j++)
            if(a[i][j]==3)printf("c");else
            if(!a[i][j])printf(".");else            
                        printf("*");
          printf("\n"); 
          }
        }
    for(i=1;i<=n;i++)
     for(j=1;j<=m;j++)a[i][j]=b[i][j]=0;
    }
// system("pause");
}
