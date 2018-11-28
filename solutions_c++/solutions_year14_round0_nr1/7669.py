#include <iostream>
#include <stdio.h>
#include <stdlib.h>


int matrixOne[5][5];
int matrixTwo[5][5];
int one,two;
int card;
 FILE *f;
 FILE *g;

int magicTrick()
{
   int res=0;


 for (int i=1;i<=4;i++)
 {
     for (int j=1;j<=4;j++)
     {
        if (matrixOne[one][i]==matrixTwo[two][j]) {res++;card=matrixOne[one][i];}
     }


 }


return res;
}

void read()
{

   fscanf (g,"%d",&one);
  for (int i=1;i<5;i++)
  {
     for (int j=1;j<5;j++)
        fscanf(g,"%d",&matrixOne[i][j]);
  }

  fscanf(g,"%d",&two);
 for (int i=1;i<5;i++)
  {
     for (int j=1;j<5;j++)
        fscanf(g,"%d",&matrixTwo[i][j]);
  }

}



int main()
{
 int test;



  g=fopen("magictrick.in.txt","r");
  f=fopen("magictrick.txt","w");


fscanf(g,"%d",&test);

for (int i=1;i<=test;i++)
{

read();
int result=magicTrick();
switch (result){
     case 0:fprintf(f,"Case #%d: Volunteer cheated!\n",i);break;
     case 1:fprintf(f,"Case #%d: %d\n",i,card);break;
     default :fprintf(f,"Case #%d: Bad magician!\n",i,card);break;
        };
    }

fclose(f);
fclose(g);
return 0;
}
