#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;
#define debug
#define min4(a,b,c,d) min(min(a,b),min(c,d))

int dp[300][300][300];
int goX,goY;

int get(int x,int y,int idx){
    
    debug("get %d %d %d\n",x,y,idx);

    if(x<0||y<0||x>=300||y>=300||idx>=200)return 9999999;
    if(dp[x][y][idx]+1)return dp[x][y][idx];
    
    if(x==goX && y==goY)return 0;
    int uu=dp[x][y][idx] = 1+min4(get(x+idx,y,idx+1),get(x-idx,y,idx+1),get(x,y+idx,idx+1),get(x,y-idx,idx+1));
 
    return dp[x][y][idx];
    
}

main(){
       
       int te;
       scanf("%d",&te);
       
       for(int t=1;t<=te;t++){
               
               memset(dp,-1,sizeof(dp));
               
               scanf("%d%d",&goX,&goY);
               
               goX+=100;
               goY+=100;
               
               int k = get(100,100,1);
               
               debug("k=%d\n",k);
               printf("Case #%d: ",t);
               
               int x=100,y=100;
               for(int i=1;i<=k;i++){
                       
                       debug("\nx=%d y=%d dp=%d\n",x,y,get(x,y,i));
                       
                       if(get(x,y,i)-1 == get(x+i,y,i+1)){
                                       putchar('E');
                                       x+=i;
                                       }
                       else if(get(x,y,i)-1 == get(x-i,y,i+1)){
                                       putchar('W');
                                       x-=i;
                                       }
                       else if(get(x,y,i)-1 == get(x,y+i,i+1)){
                                       putchar('N');
                                       y+=i;
                                       }
                       else if(get(x,y,i)-1 == get(x,y-i,i+1)){
                                       putchar('S');
                                       y-=i;
                                       }
                       else while(1);
                       
                       }
               
               printf("\n");}}
