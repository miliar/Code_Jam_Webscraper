#include <cstdio>
#include <iostream>
#include <cmath>


//X=88 O=79 .=46 T=84
// X --> 352  348
// O --> 316  321 
using namespace std;

int Table[4][4];

void init(){
    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
            Table[i][j]=3;
}

int winner(){
    //filas
    int sum=0;
    int draw=0;
    for(int i=0; i<4; i++){
        for(int x=0; x<4; x++){
            sum+=Table[i][x];
        }
        if(sum==400 || sum==350)
                return 1;
            if(sum==40 || sum == 80)
                return 2;
            if(sum%10 > 0)
                draw=1;
        sum=0;
    }
    
    
    for(int j=0; j<4; j++){
        for(int x=0; x<4; x++){
            sum+=Table[x][j];
        }
       // printf("--sum: %d\n",sum);
        if(sum==400 || sum==350)
                return 1;
            if(sum==40 || sum==80)
                return 2;
            if(sum%10 > 0)
                draw=1;
        sum=0;
    }
    
    //printf("----->\n");
    for(int i=0; i<4; i++)
        sum+=Table[i][i];
    if(sum==400 || sum==350)
        return 1;
    if(sum==40 || sum==80)
        return 2;
    if(sum%10 > 0)
        draw=1;
    sum=0;
    
        
    for(int i=0; i<4; i++)
        sum+=Table[i][3-i];
    if(sum==400 || sum==350)
        return 1;
    if(sum==40 || sum==80)
        return 2;
    if(sum%10 > 0)
        draw=1;
    sum=0;
        
   if(draw ==1) return 3;//Falta jugar
   else return 4;//Empate
}

void prin(){
    for(int x=0; x<4; x++){
      for(int i=0; i<4; i++)
        printf("%d ",Table[x][i]);    
      printf("\n");
      }
}

int main(){
    //freopen("A-small-attempt0.in","r",stdin);
    int T;
    scanf("%d",&T);
    string m;
    int tes=1;
   // while(tes <= T){
   for(int tes=1; tes<=T; tes++){
        //printf("%d\n",T);
            for(int i=0; i<4; i++){
                cin>>m;
                for(int j=0; j<4; j++){
                    if(m[j]==88)
                        Table[i][j]=100;
                    if(m[j]==79)
                        Table[i][j]=10;
                    if(m[j]==84)
                        Table[i][j]=50;
                    if(m[j]==46)
                        Table[i][j]=1;                                        
                }
            }
            //prin();   
            
            int win=winner();
            //printf("win : %d\n",win);
            if(win==1)
                printf("Case #%d: X won\n",tes);
            if(win==2)
                printf("Case #%d: O won\n",tes);
            if(win==3)
                printf("Case #%d: Game has not completed\n",tes);
            if(win==4)
                printf("Case #%d: Draw\n",tes);
                
             
            
           //tes++;
           //printf("test \n");
    }
    

    return 0;
    
}

