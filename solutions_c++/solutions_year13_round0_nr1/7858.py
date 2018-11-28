#include<stdio.h>
#include<conio.h>
#include<fstream.h>
#include<stdlib.h>

void main()
{
int game[10];
//int mainmat[200]={1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0};

int mainmat[200]={1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,111};
/*int a1[10]={1,1,0,0,0,1,0,0,0,0};
int a2[10]={0,1,0,0,0,0,1,0,0,0};
int a3[10]={0,1,0,0,0,0,0,1,0,0};
int a4[10]={0,1,0,0,0,0,0,0,1,1};//
int a5[10]={0,0,1,0,0,1,0,0,0,0};//
int a6[10]={1,0,1,0,0,0,1,0,0,0};//
int a7[10]={0,0,1,0,0,0,0,1,0,1};//
int a8[10]={0,0,1,0,0,0,0,0,1,0};//
int a9[10]={0,0,0,1,0,1,0,0,0,0};//
int a10[10]={0,0,0,1,0,0,1,0,0,1};//
int a11[10]={1,0,0,1,0,0,0,1,0,0};//
int a12[10]={0,0,0,1,0,0,0,0,1,0};//
int a13[10]={0,0,0,0,1,1,0,0,0,1};//
int a14[10]={0,0,0,0,1,0,1,0,0,0};//
int a15[10]={0,0,0,0,1,0,0,1,0,0};//
int a16[10]={1,0,0,0,1,0,0,0,1,0};
*/
int x,y,n,i,j,temp,Tcount,k,T,l,count,index;
char line[10];
ifstream f1;
ofstream f2;
clrscr();
f1.open("A-large.in");
f2.open("outputxxx.txt") ;
//printf("%d",mainmat[170]);

if(f1==0)
{
printf("error");
}

f1.getline(line,10);
n=atoi(line);
//printf("\n%d",n);

for(j=0;j<n;j++)
{
	for(x=0;x<10;x++)
       {	game[x]=0;   }
	T=200;
	count=0;

     for(i=0;i<4;i++)
     {
	f1.getline(line,20);
//	printf("\n%s",line);

	///// For calculation of 'X' Increament
		for(y=0;y<4;y++)
		{        if(line[y]!='.')
			 { count++; }

			 if(line[y]=='X')
			 {
				index=(y+(i*4))*10;
				for(k=0;k<10;k++)
				{
				game[k]=game[k]+mainmat[index]  ;
				index++;
				}
			 }
			 else if(line[y]=='O')
			 {
				index=(y+(i*4))*10;
				for(k=0;k<10;k++)
				{
				game[k]=game[k]-mainmat[index];
				index++;
				}
			 }
			 else if(line[y]=='T')
			 {
				 T=(y+(i*4))*10;
			 }



		 }
     }
temp=T;
Tcount=0;
CHECK:

      for(l=0;l<10;l++)
      {
		if(game[l]==4)
		{
		printf("Case #%d: X won\n",j+1);
		f2<<"Case #"<<j+1<<": X won\n";
		goto END;
		}
		else if(game[l]==-4)
		{
		printf("Case #%d: O won\n",j+1);
		f2<<"Case #"<<j+1<<": O won\n";
		goto END;
		}
      }
//  Condition for T
      if (T!=200)
      {
      Tcount++;
      T=temp;
	if(Tcount==1)
	{
		 for(k=0;k<10;k++)
		   {
			game[k]=game[k]+mainmat[T]  ;
			T++;
		   }
		  goto CHECK;
	}
	else if(Tcount==2)
	{
		 for(k=0;k<10;k++)
		   {
			game[k]=game[k]-(2*mainmat[T])  ;
			T++;
		   }
		  goto CHECK;
	}




      }


      if(count==16)
      {
      printf("Case #%d: Draw\n",j+1);
      f2<<"Case #"<<j+1<<": Draw\n";
      }
      else
      {
      printf("Case #%d: Game has not completed\n",j+1);
      f2<<"Case #"<<j+1<<": Game has not completed\n";
      }

END:
f1.getline(line,20);
//printf("\n%s",line);

}

getch();
}