
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <fstream>
using namespace std;


int main()
{


int T;

int a[4][4];
char c;
char c1[4][4];
char p[100];
int i=0,j=0,k=0;
int w=0;
int g=0;
int X1,O1;
int X2,O2;

int DX1=0;
int DX2=0;
int DO1=0;
int DO2=0;

FILE *fp;
FILE *out;

fp=fopen("a.in","r");

ofstream outfile("k.txt");

fscanf(fp,"%d\n",&T);


for(i=0;i<T;i++){

w=0;
g=0;

   for(j=0;j<4;j++)
    {
     
     for(k=0;k<4;k++)
        {
         fscanf(fp,"%c",&c);
         c1[j][k]=c; 
         if(c=='X'){a[j][k]=1; } 
         else if(c=='O'){a[j][k]=0;}
         else if(c=='T'){a[j][k]=-1;}
         else {a[j][k]=-2;g=1;}  
        }
    fscanf(fp,"\n");
    }


DX1=0;
DX2=0;
DO1=0;
DO2=0;


  for(j=0;j<4;j++)
   {

X1=0;
O1=0;

X2=0;
O2=0;

    
     for(k=0;k<4;k++)
	{
	
	if(a[j][k]==1 || a[j][k]==-1){X1++;}
   	
        if(a[j][k]==0 || a[j][k]==-1){O1++;}


        if(a[k][j]==1 || a[k][j]==-1){X2++;}
   	
        if(a[k][j]==0 || a[k][j]==-1){O2++;}
        
        if(j==k ){


             if(a[j][k]==1 || a[j][k]==-1){DX1++;}
   	
              if(a[j][k]==0 || a[j][k]==-1){DO1++;}


            }

      if(j+k==3 ){


             if(a[j][k]==1 || a[j][k]==-1){DX2++;}
   	
              if(a[j][k]==0 || a[j][k]==-1){DO2++;}


            }


         }

    if((X1==4 || X2==4) && w==0){
      //fprintf(fp2,"Case #%d: X won\n",i+1);
      outfile<<"Case #"<<i+1<<": X won"<<endl;
      w=1;
     }
	
    if((O1==4 || O2==4)  && w==0){
      //fprintf(fp2,"Case #%d: O won\n",i+1);
       outfile<<"Case #"<<i+1<<": O won"<<endl;
       w=1;
     }


    }

 
    if((DX1==4 || DX2==4)  && w==0){
      //fprintf(fp2,"Case #%d: X won\n",i+1); 
    outfile<<"Case #"<<i+1<<": X won"<<endl;
   w=1;
     }
	
    if((DO1==4 || DO2==4)  && w==0){
     // fprintf(fp2,"Case #%d: O won\n",i+1);
    outfile<<"Case #"<<i+1<<": O won"<<endl;
w=1;
     }


if(w==0 && g==0){//fprintf(fp2,"Case #%d: Draw\n",i+1); 

  outfile<<"Case #"<<i+1<<": Draw"<<endl;
}
if(w==0 && g==1){//fprintf(fp2,"Case #%d: Game has not completed\n",i+1); 

  outfile<<"Case #"<<i+1<<": Game has not completed"<<endl;


}



fscanf(fp,"\n");



}


fclose(fp);
//fclose(fp2);


return 0;
}
