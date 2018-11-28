#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
int main(){

int t;
char b[5][5] = {"."};
int ans = -1;
char p;

scanf("%d\n",&t);
for (int i=0; i<t; i++){
         for (int j=0; j<4; j++){
             for (int k=0; k<4; k++)
                 scanf("%c",&b[j][k]);
             
              scanf("%c",&p);
              }    
ans = -1;

for(int a=0; a<4; a++){
   if( ( (b[a][0] == 'X' || b[a][0] == 'T') && 
         (b[a][1] == 'X' || b[a][1] == 'T') && 
         (b[a][2] == 'X' || b[a][2] == 'T') && 
         (b[a][3] == 'X' || b[a][3] == 'T')
        )   ||
       ( (b[0][a] == 'X' || b[0][a] == 'T') && 
         (b[1][a] == 'X' || b[1][a] == 'T') && 
         (b[2][a] == 'X' || b[2][a] == 'T') && 
         (b[3][a] == 'X' || b[3][a] == 'T')  
        )   ||
       ( (b[0][0] == 'X' || b[0][0] == 'T') && 
         (b[1][1] == 'X' || b[1][1] == 'T') && 
         (b[2][2] == 'X' || b[2][2] == 'T') && 
         (b[3][3] == 'X' || b[3][3] == 'T')  
        )   ||
       ( (b[0][3] == 'X' || b[0][3] == 'T') && 
         (b[1][2] == 'X' || b[1][2] == 'T') && 
         (b[2][1] == 'X' || b[2][1] == 'T') && 
         (b[3][0] == 'X' || b[3][0] == 'T')  
        ) 
       
      )      
      ans = 1;
}
if (ans == -1) {
for(int a=0; a<4; a++){
   if( ( (b[a][0] == 'O' || b[a][0] == 'T') && 
         (b[a][1] == 'O' || b[a][1] == 'T') && 
         (b[a][2] == 'O' || b[a][2] == 'T') && 
         (b[a][3] == 'O' || b[a][3] == 'T')
        )   ||
       ( (b[0][a] == 'O' || b[0][a] == 'T') && 
         (b[1][a] == 'O' || b[1][a] == 'T') && 
         (b[2][a] == 'O' || b[2][a] == 'T') && 
         (b[3][a] == 'O' || b[3][a] == 'T')  
        )  ||
       ( (b[0][0] == 'O' || b[0][0] == 'T') && 
         (b[1][1] == 'O' || b[1][1] == 'T') && 
         (b[2][2] == 'O' || b[2][2] == 'T') && 
         (b[3][3] == 'O' || b[3][3] == 'T')  
        )   ||
       ( (b[0][3] == 'O' || b[0][3] == 'T') && 
         (b[1][2] == 'O' || b[1][2] == 'T') && 
         (b[2][1] == 'O' || b[2][1] == 'T') && 
         (b[3][0] == 'O' || b[3][0] == 'T')  
        )
      )   
      ans = 2;
}}

if (ans == -1) {
for(int a=0; a<4; a++){
        for(int c=0; c<4; c++){
                if(b[a][c] == '.'){
                           ans = 4;
                }
        }
}}
if (ans == -1) ans = 3;

if (ans == 1) printf("Case #%d: X won\n", i+1);
if (ans == 2) printf("Case #%d: O won\n", i+1);
if (ans == 3) printf("Case #%d: Draw\n", i+1);
if (ans == 4) printf("Case #%d: Game has not completed\n", i+1);
scanf("%c",&p);
}
  
//system("pause");
return 0;                  
}
