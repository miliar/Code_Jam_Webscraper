#include<iostream>
#include<fstream>
#include<stdio.h>

using namespace std;

void Input();
fstream fs,os;
float maxKen(float[],int *),minKen(float[],int *),minNaomi(float[],int *),maxNaomi(float[],int *);
int t,val=1,no,minIndKen,maxIndKen,minIndNaomi,maxIndNaomi,minIndKen2,maxIndKen2,minIndNaomi2,maxIndNaomi2,scrD=0,scrW=0;
float naomi[1000],ken[1000],naomi2[1000],ken2[1000];
	
void main()
{
	float kenMax,kenMin,naomiMin,naomiMax,kenMax2,kenMin2;
	int i=0;	

	fs.open("war3.in",ios::in);
	os.open("sol3.txt",ios::out);
	

	fs>>t;

	while(t>0)
	{
		
	Input();
	i=0;
	while(i<no)
	{
		naomi2[i]=naomi[i];
		ken2[i]=ken[i];
		i++;
	}
	i=0;
	while(i<no)
	{

	kenMax=maxKen(ken,&maxIndKen);
	kenMax2=maxKen(ken2,&maxIndKen2);
	kenMin=minKen(ken,&minIndKen);
	kenMin2=minKen(ken2,&minIndKen2);
	naomiMin=minNaomi(naomi,&minIndNaomi);
	naomiMax=maxNaomi(naomi2,&maxIndNaomi2);

	if(naomiMin>kenMin)
		{
			scrD++;
			naomi[minIndNaomi]=-1;
			ken[minIndKen]=-1;
	}

	else 
	{
		ken[maxIndKen]=-1;
		naomi[minIndNaomi]=-1;
		
	}	
	
	if(kenMax2>naomiMax)
	{
		ken2[maxIndKen2]=-1;
		naomi2[maxIndNaomi2]=-1;
	}

	else if(kenMax2<naomiMax)
	{
		ken2[minIndKen2]=-1;
		naomi2[maxIndNaomi2]=-1;
				scrW++;
	}

	
		i++;
	}

	os<<"Case #"<<val<<": "<<scrD<<" "<<scrW<<"\n";
	t--;

	val++;
	
	}
	fs.close();
	os.close();
		
}


void Input()
{
	scrD=0;scrW=0;
	fs>>no;
	int i=0;

	while(i<no)
			fs>>naomi[i++];
	
	i=0;
	while(i<no)
		fs>>ken[i++];
}

float maxKen(float ken[],int *index)
{
	float max=0;
	int i=0;
	while(i<no)
		{
			if(ken[i]!=-1)
			{
			if(ken[i]>max)
			{
				max=ken[i];
				*index=i;
			}

			
	}
			i++;
	}
	return max;
}

float minKen(float ken[],int *index)
{
	float min=1.0;
	int i=0;
	while(i<no)
		{
			if(ken[i]!=-1)
			{
			if(ken[i]<min)
			{
				min=ken[i];
				*index=i;
			}

			
	}
			i++;
	}

	return min;
}

float minNaomi(float naomi[],int *index)
{
	float min=1.0;
	int i=0;
	while(i<no)
	{
		if(naomi[i]!=-1)
		{
		if(naomi[i]<min)
			{
				min=naomi[i];
				*index=i;
		}
		
	}
		i++;
	}

	return min;
}

float maxNaomi(float naomi[],int * index)
{
	float max=0.;
		int i=0;

	while(i<no)
	{
		if(naomi[i]!=-1)
		{
			if(naomi[i]>max)
				{
					max=naomi[i];
					*index=i;
			}
		}
		i++;
	}
	return max;
}
	
	


	


	


