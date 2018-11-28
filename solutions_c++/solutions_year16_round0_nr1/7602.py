#include<stdio.h>



void main()
{
FILE *fr,*fw;




int T,N,j,i=0,k=0,flag=0,Last,D[9],x,Z   ;


fr=fopen("sheep.txt","r");
fw=fopen("Outputsheep.txt","a");
fscanf(fr,"%d", &T);
for( k=1; k<=T; k++)
{
flag=0;
fscanf(fr,"%d", &N) ;
if(N==0)
fprintf(fw,"Case #%d: INSOMNIA",k);

else
{  for(i=0; i<9;i++)
   D[Z]=10;
   i=1;
   while(1)
   { i++;
     x=N*i;
    while(x)
    { Z=x%10;
      if(D[Z]==10)
       { D[Z]=1;
         flag++;
       }
      x=x/10;


    Last=D[Z];
    }
   if(flag==9)
   { fprintf(fw,"Case #%d: %d\n",k,Last);
   break;
   }
   }

}
}
fclose(fr);
fclose(fw);
}




