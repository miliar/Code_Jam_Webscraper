#include <cstdio>
#include <string>
#include <math.h>

using namespace std;
long long M;

long long A,B,N,R,Q,QQ,F,G;
long long int posi,pos ;
int i,j,L,LL,ini,inj,ban,CONTA;
int C[100],D[100];
/*
void escribirnumero(void)
{    printf("\n C: ");
     for(i=L-1;i>=0;i--)
       printf("%d ",C[i]);     
       
}*/
void probarcapicua()
{
    i=ini;j=inj;
    ban=0;
    while(i<L && ban==0){
       if(C[i]==C[j]) {i++;j--;}
       else ban=1;
    }
    if(ban==0){ //conta++;// printf(" \n-UN1 palindromo+++");
    }
    else { // printf(" \n-un NO HAY palindromo+++");
    }
}
void generarinicial()
{
   
   i=0;
   while(M>0){
       C[i]=M%10;
       M=(M-C[i])/10;
       
  
       i++;
       
   }
    
   L=i;
   
   if(L%2==0){
       ini=L/2; inj=ini-1;
    }             
    else{ ini=(L-1)/2; inj=ini;
   }
   

}
void generarQ(){
   Q=0;
   G=1;
   for(i=0;i<L;i++){
       F=1;
       for(j=0;j<L;j++){
       Q=Q+C[i]*C[j]*F*G;
       F=F*10;
       }
       G=G*10;
   }
  // printf("\nVALOR DE Q: %d",Q);
   QQ=Q;
}
void esQpalindromo()
{   
    i=0;
    while( Q>0 ){
       D[i]=Q%10;
       Q=(Q-D[i])/10;
       
   //    printf(" \nxx- C: %d -- %d",C[i],i);
       i++;      
     }
     LL=i;
   
     i=0;
    ban=0;
    while(i<LL && ban==0){
       if(D[i]==D[LL-i-1]) {i++;}
       else ban=1;
    }
    if(ban==0){ CONTA++; //printf(" \n-CONTA+++");
    }
    else {  //printf(" \nNO SE CONTA");
    }
     
    
}
void buscarpalindromo()
{
   i=ini;j=inj;
   while(i<L && C[i]==C[j]){
   i++;j--;          
   }
   if(i<L){
      if(C[i]>C[j]) ban=1;
      else ban=0;
      
      while(i<L) {
      C[j]=C[i];i++;j--;
      }
      if(ban==1) { 
         // printf(" \n-probar nuev capicua");
         
      //   escribirnumero();
         generarQ();
         if(Q<=B)
         esQpalindromo();
         
         //probarcapicua();
      }
      
   }
   else{
      //printf(" \n-probar capicua");
      // escribirnumero();
        generarQ();
        if(Q<=B)
         esQpalindromo();
         //probarcapicua();
   }

}

void siguientepalindromo( void){
  i=ini; j=inj; 
  while(i<L && C[i]==9){
     C[i]=0; C[j]=0; i++; j--;
  }   
   if(i<L){
      if(i==j){ C[i]++;
      }
      else {  C[i]++; C[j]++ ;
      }
   }
   else{
      C[L]=1;
      C[0]=1;
      L++;
      if(L%2==0){
         ini++;
      }
      else{
           inj++;
      }
   
   }
}
int main(int argc, char **argv) {
   
 
int TT; 
int I=1;
 
 scanf("%d", &TT);
while(I<=TT)
 {  
   scanf("%d %d", &A, &B);
  //  A=985432664;
  //  B=14800;
  CONTA=0;
   //Q=1;
    M=(int)sqrt(A);
    if (A>M*M) M++;
    //M=1;
  //  printf(" \n MMMMM %d",M);
    
   generarinicial();
   
     
  
      
    buscarpalindromo();
    
       	
       	
    siguientepalindromo();
   // escribirnumero();

       	
       	generarQ();
       	
   while( QQ <= B )  {
      //if(Q==1) 
      // printf(" \n- ENTRO-"); 
       
       esQpalindromo();
//        scanf("%d", &N);
       
      siguientepalindromo();           
    //  escribirnumero();
      generarQ();
      
      
      
        
   }
   
     
    //siguientepalindromo();
	
    printf("Case #%d: %d\n",I,CONTA); 
	
	I++;
  }
	
//	scanf("%d", &N);
	return 0;
}

