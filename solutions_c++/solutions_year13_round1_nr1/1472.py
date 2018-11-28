#include <stdio.h>
#include <stdlib.h>

int main(){
    int n,N,r,t,j;
    FILE* bob;
    bob=fopen("ansA.txt","w");
    scanf("%d",&N);
    for(n=0;n<N;n++)
    {
        scanf("%d %d",&r,&t);
        for(j=1;j>0;j++)
        {
           if(t>=(2*r+4*j-3)){
              t-=2*r+4*j-3;
           }
           else
             break;                
        }       
        j--;
        fprintf(bob,"Case #%d: %d\n",n+1,j);              
    }
    fclose(bob);
    system("pause");    
    return 0;
}

