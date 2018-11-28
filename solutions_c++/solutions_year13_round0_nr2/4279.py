#include <cstdio>
#include <string>

using namespace std;
int esta,bx,by;



int main(int argc, char **argv) {

	
	int NN,in,N,M,i,j;
    int A[105][105],ban,Min;
  	
    in=1; //NN=1; 
    scanf("%d", &NN);
    while ( in<=NN ){
          //printf(" \nESTAdo:-- %d ----", esta); 
          
          ban=1;
          scanf("%d %d", &N , &M);
          for(i=0;i<N;i++)
             for(j=0;j<M;j++)
                scanf("%d", &A[i][j]);
          
          for(i=0;i<N;i++) A[i][M]=0;
          for(j=0;j<M;j++) A[N][j]=0;
          
          
          for(i=0;i<N;i++)
             for(j=0;j<M;j++){
             if(A[i][j]>A[N][j]) A[N][j]=A[i][j];
             } 
          
          for(i=0;i<N;i++)
             for(j=0;j<M;j++){
             if(A[i][j]>A[i][M]) A[i][M]=A[i][j];
             } 
          
          for(i=0;i<N;i++)
             for(j=0;j<M;j++){
                if( A[i][M]<A[N][j] ) Min=A[i][M];
                else Min=A[N][j];
                
                if (A[i][j]==Min) ;
                else {
                ban=0; i=N;j=M;
                }
             }
         
         
         if(ban==1)                     
           printf("Case #%d: YES\n", in);    
         else
           printf("Case #%d: NO\n", in);              
                       
          
          
          //ESCRIBIR
       /*   
          for(i=0;i<=N;i++){
             for(j=0;j<=M;j++)
                printf("%d ", A[i][j]);
            printf("\n");
          }*/
          in++;
    }
    
    
	// scanf("%d", &NN);	
	return 0;
}

