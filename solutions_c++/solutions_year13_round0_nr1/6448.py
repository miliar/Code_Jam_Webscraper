#include<stdio.h>
#include<string.h>
int main()
{
  char b[4][4];
  int board[4][4]={0};
  int t,i,j,sumr=0,sumc=0,sumd=0,sumdd=0,flag=0,fflag=0,result[1001]={0};
  int cas=0;
  FILE* r=NULL;
  FILE* w=NULL;
  w=fopen("C:\\output.txt","w");
  r=fopen("C:\\file.txt","r");
  fscanf(r,"%d",&t);
  while(t!=cas)
  {
  	sumr=0;sumc=0;sumd=0;sumdd=0;flag=0;fflag=0;
  for(i=0;i<4;i++)
  {
   for(j=0;j<4;j++)
   {
    fscanf(r,"%c",&b[i][j]);
    if(b[i][j]=='X')
    board[i][j]=2;
    else if((b[i][j]=='O'))
    board[i][j]=-2;
    else if((b[i][j]=='T'))
    board[i][j]=1;
    else if((b[i][j]=='.'))
    board[i][j]=55;
    else if((b[i][j]=='\n'))
    j--;
   }
  }
   for(i=0;i<4;i++)
   {
    for(j=0;j<4;j++)
    {
    	if(board[i][j]==55) flag=1;
    sumr=sumr+board[i][j];
	sumc=sumc+board[j][i]; 
    }
    
    if((sumr<=8&&sumr>=7)||(sumc<=8&&sumc>=7))
    { result[cas++]=1; fflag=1;break;}
    else if((sumc<=-5||sumr<=-5))
    { /*fprintf(w,"ans %d %d %d %d\n",i,j,sumr,sumc); */result[cas++]=2; fflag=1;break;}
    sumc=0;sumr=0;
   }
   if(!fflag)
	{
	for(i=0;i<4;i++)
   {
    for(j=0;j<4;j++)
    { 
    if(i==j)
    sumd=sumd+board[i][j];
    if((i+j)==3)
    sumdd=sumdd+board[i][j];
    }
   }
	
   if((sumd<=8&&sumd>=7)||(sumdd<=8&&sumdd>=7))
    { result[cas++]=1; fflag=1;}
   else if(sumd<=-5||sumdd<=-5)
    { /*fprintf(w,"ans : %d %d %d %d\n ",i,j,sumd,sumdd);*/ result[cas++]=2; fflag=1;}
	}
   if(!fflag)
   if(flag)
   result[cas++]=3;
   else
   result[cas++]=4;
}
for(cas=0;result[cas]!=0;cas++)
{
	fprintf(w,"Case #%d:",cas+1);
switch(result[cas])
{
	case 1: fprintf(w," X won\n");
	break;
	case 2: fprintf(w," O won\n");
	break;
	case 3: fprintf(w," Game has not completed\n");
	break;
	case 4: fprintf(w," Draw\n");
	break;
}
}
fclose(r);
fclose(w);
}

