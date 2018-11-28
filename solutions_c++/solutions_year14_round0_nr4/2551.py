#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;

int warcount = 0;
int dwarcount = 0;
int stick;
double N[1005],K[1005];

void compare(int a,int b)
{
	if(N[a]>K[b])
	{
		warcount++;
		if(a>0)
			compare(a-1,b);
	}
	else
	{
		if(a>0 && b>0)
			compare(a-1,b-1);
	}
}

void compare2(int a,int b)
{
	if(N[a]>K[b])
	{
		dwarcount++;
		if(a<stick-1 && b<stick-1)
			compare2(a+1,b+1);
	}
	else
	{
		if(a<stick-1)
			compare2(a+1,b);
	}
}

int cmp(const void *a, const void *b)
{
	return(*(double *)a) > (*(double *)b) ? 1 : -1;
}



int main ()
{
	ifstream R("D-large.in");
    ofstream W("D-large.out");
    
    int t;
    R>>t;

    for (int ti=1;ti<=t;++ti)
    {
    	warcount = 0;
    	dwarcount = 0;
    	
		R>>stick;
		for(int i = 0; i<stick ;i++)
		{
			R>>N[i];
		}
		for(int i = 0; i<stick ;i++)
		{
			R>>K[i];	
		}
			
		qsort(&N[0],stick,sizeof(N[0]),cmp);
		qsort(&K[0],stick,sizeof(K[0]),cmp);
    	
    	compare(stick-1,stick-1);
		compare2(0,0);

		W<<"Case #"<<ti<<": "<<dwarcount<<" "<<warcount<<endl;
	}
}

