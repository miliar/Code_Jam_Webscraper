#include <stdio.h>
#include <stdlib.h>
int main(void){
    int T, i,j,k,l,z,ansx,ansy,maze[300][300],n,m,ans;
    scanf("%d",&T);
    FILE* bob;
    bob=fopen("b.txt","w");
    for(z=0;z<T;z++)
    {
      scanf("%d %d",&n,&m);
      for(i=0;i<n;i++){
         for(j=0;j<m;j++){
            scanf("%d",&maze[i][j])   ;           
         }
      }
      ans=0;
      for(i=0;i<n;i++){
         for(j=0;j<m;j++){
                          //dot
            ansx=0;
            ansy=0;
            
            for(k=0;k<n;k++)
            {
              if(maze[k][j]>maze[i][j])    
              {
                ansx=2;      
              } 
            }
            for(k=0;k<m;k++)
            {
              if(maze[i][k]>maze[i][j])    
              {
                ansy=2;       
              }            
            }
            if(ansx*ansy==4){
                fprintf(bob,"Case #%d: NO\n",z+1);
                ans=1;
                i=100000;
                j=100000;
                break;
                     
            }           
         }
      }
      if(ans==0)
      fprintf(bob,"Case #%d: YES\n",z+1);
      ppp:
          ;
    }
    fclose(bob);
    system("pause");
    return 0;
}
