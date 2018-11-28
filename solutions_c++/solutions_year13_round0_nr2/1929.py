#include<cstdio>
#include<cstring>
using namespace std;
int N,M,grass[105][105];
bool val(int x,int y)
{
   int i,j;
   bool f=true;
   if(x>0){
   for(i=0; i<x; i++)
     if(grass[y][i]>grass[y][x]) f=false;
     }
   if(x<M-1){
   for(i=x+1; i<M; i++)
     if(grass[y][i]>grass[y][x]) f=false;
     }
   if(f) return true;
   f=true; 
   if(y>0){ 
   for(i=0; i<y; i++)
     if(grass[i][x]>grass[y][x]) f=false;
     }
   if(y<N-1){
   for(i=y+1; i<N; i++)
     if(grass[i][x]>grass[y][x]) f=false;
     }
   if(f) return true;
   
   return false;
}
bool Vallid()
{
   int i,j;
   for(i=0; i<N; i++)
     for(j=0; j<M; j++)
     {
        bool f=val(j,i);
        if(f==false) return false;      
     } 
  return true;  
}
int main()
{
    int i,j,k,T,c=0;
    //freopen("B-large.in","r",stdin);
    //freopen("outB1.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
       scanf("%d%d",&N,&M);
       for(i=0; i<N; i++)
         for(j=0; j<M; j++)
            scanf("%d",&grass[i][j]); 
            
       bool f=Vallid();
       if(f) printf("Case #%d: YES\n",++c);
       else printf("Case #%d: NO\n",++c);     
    }
    return 0;
}
