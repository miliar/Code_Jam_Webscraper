#include <stdio.h>

main()
{
 char A[4][4], vencedor, letra,espaco[5];
 int cont, T, i, j, caso, aux;	
 bool acabou, draw; 
 
 scanf("%d\n", &T);

 for(caso=1;caso<=T;caso++)
 {  
  draw=true;	 
  acabou=false;	 
  for(i=0;i<4;i++)
  {	 
   gets(A[i]);
   letra='.';
   j=-1;
   aux=0;

   while(letra=='.')
    {
     j++;
     letra=A[i][j];
     if(letra=='T')
      {letra='.'; aux++;}
     if(letra=='.')
      draw=false;
    }
 

   for(;j<4;j++)
   {
	if((A[i][j]==letra)||(A[i][j]=='T'))
	 aux++;
   }

   if(aux==4)
    {printf("Case #%d: %c won\n", caso, letra); acabou=true;}
  } //lê e verifica se tem um ganhador numa LINHA;
  
  gets(espaco);

  if(acabou)
   continue;   
   
   for(i=0;i<4;i++)
  {	 
   letra='.';
   j=-1;
   aux=0;

   while(letra=='.')
    {
     j++;
     letra=A[j][i];
     if(letra=='T')
      {letra='.'; aux++;}
     if(j==3)
      break;
    }  

   for(;j<4;j++)
   {
	if((A[j][i]==letra)||(A[j][i]=='T'))
	 aux++;
   }

   if(aux==4)
    {printf("Case #%d: %c won\n", caso, letra); acabou=true; break;}
  }//verifica se há vencedor em uma coluna;
   
  if(acabou)
   continue;
  
  if(A[0][0]=='T')
   A[0][0]=A[1][1];
  else if(A[1][1]=='T')
   A[1][1]=A[2][2];  
  else if(A[2][2]=='T')
   A[2][2]=A[3][3];  
  else if(A[3][3]=='T')
   A[3][3]=A[2][2];  
 
   if((A[0][0]==A[1][1])&&(A[2][2]==A[1][1])&&(A[2][2]==A[3][3])&&(A[1][1]!='.'))
    {printf("Case #%d: %c won\n", caso, A[0][0]); continue;}
   
  if(A[0][3]=='T')
   A[0][3]=A[1][2];
  else if(A[1][2]=='T')
   A[1][2]=A[2][1];  
  else if(A[2][1]=='T')
   A[2][1]=A[3][0];  
  else if(A[3][0]=='T')
   A[3][0]=A[2][1];  

  if((A[0][3]==A[1][2])&&(A[1][2]==A[2][1])&&(A[2][1]==A[3][0])&&(A[3][0]!='.'))
   {printf("Case #%d: %c won\n", caso, A[3][0]); continue;}
   
  if(draw) 
   {printf("Case #%d: Draw\n", caso); continue;}
  else
   {printf("Case #%d: Game has not completed\n", caso); continue;}
 }
}
