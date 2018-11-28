#include<stdio.h>

int T,normal,cambio,unico,bandera,cont;
int cards1[6][6],cards2[6][6];

int main(){
 scanf("%d",&T);
 for(int k=1;k<=T;k++){
    cont=0;
    bandera = 1;

    scanf("%d",&normal);
    for(int i=1;i<=4;i++)
       for(int j=1;j<=4;j++)
          scanf("%d",&cards1[i][j]);
    scanf("%d",&cambio);

    for(int i=1;i<=4;i++)
       for(int j=1;j<=4;j++)
          scanf("%d",&cards2[i][j]);

    for(int i=1;i<=4;i++){
       for(int j=1;j<=4;j++){
          
          if(cards1[normal][i] == cards2[cambio][j]){
             cont++;
             if(bandera==1)
                unico = cards1[normal][i];
             bandera++;
          }
       }
    }
    if(cont==1)
       printf("Case #%d: %d\n",k,unico);
    else if(cont>1 && cont<5)
       printf("Case #%d: Bad magician!\n",k);
   else if(cont==0)
       printf("Case #%d: Volunteer cheated!\n",k);
 }

 return 0;
}
