#include<iostream.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<conio.h>
#define MAX 100

float pal(char[]);

void main()
{
	int num;
	clrscr();
	char numb[5];
	float res=0.0,res2=0.0;
	int start[MAX],end[MAX],count[MAX];
	double srt=0.0,res1=0.0,y=0.0;
	int i,j;

	cin>>num;
	for(i=0;i<num;i++)
	{
		cin>>start[i]>>end[i];
		count[i]=0;
	}

	for(i=0;i<num;i++)
	{
		for(j=start[i];j<=end[i];j++)
		{
			 itoa(j,numb,10);
			 res=pal(numb);
			 srt=(double)sqrt(j);
			 res1=modf(srt,&y);
			 itoa(srt,numb,10);
			 res2=pal(numb);
			 if(res==1.0 && res1==0.0 && res2==1.0)
				count[i]+=1;
		}
	}
	for(i=0;i<num;i++)
	{
		cout<<"\nCase #"<<i+1<<": "<<count[i];
	}
	getch();
}

float pal(char numb[5])
{
	char numb2[5];
	strcpy(numb2,numb);
	strrev(numb);
	if(strcmp(numb,numb2)==0)
		return 1.0;
	else return 0.0;
}