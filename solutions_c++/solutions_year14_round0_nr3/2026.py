#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std; 
#define N 5
int grid[N][N];
int ans[N][N];
int n,m;
bool f;
int ax[]={-1,-1,-1,1,1,1,0,0},by[]={0,1,-1,0,1,-1,1,-1};
bool check(int x,int y ){
     return x>=0&&x<n&&y>=0&&y<m;
}
int tmp[N][N];
// (x,y) ¿ªÊ¼ËÑË÷ 
void dfs(int x,int  y){
   // printf("%d333%d\n",x,y);
    if(ans[x][y]==1) return;
    ans[x][y]=1;
    if(tmp[x][y]) return;
    for(int i=0;i<8;i++){
            int tox=ax[i]+x,toy=by[i]+y;
           // printf("(%d,%d)",tox,toy);
            if(!check(tox,toy))continue;
           // printf("%dddd%d\n",tox,toy);
            if(grid[tox][toy]==1) continue;
            /*if(tmp[tox][toy]) {
                              ans[tox][toy]=1;
                              puts("fj");
            } 
            else*/
            dfs(tox,toy);
    }
}  
int ansx,ansy;          

void pre(){

     memset(tmp,0,sizeof(tmp));
     for(int i=0;i<n;i++){
             for(int j=0;j<m;j++){
                     if(grid[i][j]==1){
                     int x=i,y=j;
                          for(int e=0;e<8;e++){
                                 int tox=ax[e]+x,toy=by[e]+y;
                                 if(!check(tox,toy))continue;
                                 tmp[tox][toy]=1;
                          }
                     }
             }
   }
}
void out(int grid[N][N]){
     for(int i=0;i<n;i++){
             for(int j=0;j<m;j++){
                     printf("%d",grid[i][j]);
             }puts("");
     }
} 
bool check(){
    // puts("grid");
    // out(grid);
     pre();                         
    // puts("num");
   //  out(tmp);
     for(int i=0;i<n;i++){
             for(int j=0;j<m;j++){
                     if(grid[i][j]==0){
                          memcpy(ans,grid,sizeof(grid));

                         
                          //ans[i][j]=1;                                     
                          ansx=i,ansy=j;
                          dfs(i,j);
                          int tf=true;
                         // printf("%d %d\n",ansx,ansy);
                          //puts("ans");
                         // out(ans);
                          for(int ii=0;ii<n;ii++){
                                   for(int jj=0;jj<m;jj++){
                                            if(ans[ii][jj]==0) tf=false;
                                   }
                          }
                          if(tf) return true;
                     }
             }
     }    
     return false;
} 

void getGrid(int i,int x){
    if(f) return;
    if(x<0) return;
    if(x>n*m-i) return;
    //if(i>n*m) return;
    if(i==n*m&&x==0){
        if(check()) f=true;    
        return;
    }
    if(i==n*m) return;
    grid[i/m][i%m]=1;
    getGrid(i+1,x-1);
    if(f) return;
    grid[i/m][i%m]=0;
    getGrid(i+1,x);
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T,cas=1;
    scanf(" %d",&T);
    while(T--){
               scanf(" %d %d",&n,&m);
               f=false;
               int X;
               scanf(" %d",&X);
              
               memset(grid,0,sizeof(grid));
               getGrid(0,X);
               printf("Case #%d:\n",cas++);
               if(f){
                     for(int i=0;i<n;i++){
                             for(int j=0;j<m;j++){
                                     if(i==ansx&&j==ansy){
                                           putchar('c');
                                     }else if(grid[i][j]){
                                           putchar('*');
                                     }else{
                                           putchar('.');
                                     }
                             }
                             puts("");
                     }
               }else{
                      puts("Impossible");
               }
                        
    }  
   // system("pause");  
    return 0;
}
                     
                     
