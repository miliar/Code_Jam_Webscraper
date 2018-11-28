#include<iostream>
#include<conio.h>
#include<string.h>
#include<fstream>
#include<string>
#include<vector>
#include<utility>
#include<iomanip>
#include<math.h>
using namespace std;
int war(float na[],float k[],int n)
{int i,r=0,count,re=0;
for(count=0;count<n;++count)
		{
			
		if(na[count]>k[count])
	    {	
			re++;
		}
		else
		{r=n-1;
		while(r>count)
			{   
				na[r]=na[r-1];
				r--;
		    }
		}
	 }

	return re;
}

void main()
	{ 
		ifstream fin;
        fstream fout;
	fin.open("D-large.in");
    fout.open("blow.out");
      float x[1000],y[1000];
	int t,n,flag=0;
	fin>>t;
	float naomi[1000],ken[1000];

	for(int w=0;w<t;++w)
		{
		 fin>>n;
         for(int i=0;i<n;i++)
		 {
			 fin>>naomi[i];
		 }
		 for(int i=0;i<n;i++)
		 {
			 fin>>ken[i];
		 }
		 float temp;for (int x = 0; x < n-1; x++)

		for (int j = x+1; j < n; j++)

			if (naomi[x] < naomi[j])
			{
				temp = naomi[x];
				naomi[x] = naomi[j];
				naomi[j] = temp;
			}
			

	
	for(int x=0;x<n-1;++x)
	{
	for(int j=x+1;j<n;++j)
	{
	if(ken[x]<ken[j])
	       {
		temp=ken[x];
		ken[x]=ken[j];
		ken[j]=temp;
	}
	}
	}
	for(int q=0;q<n;q++)
			{x[q]=naomi[q];
	y[q]=ken[q];
	}
	   flag=war(x,y,n);
	 
	int retu=0,count,r;
	 for(count=0;count<n;++count)
		{
			
		if(naomi[count]>ken[count])
	    {	r=n-1;
			retu++;
		while(r>count)
			{   
				ken[r]=ken[r-1];
				r--;
		    }
		}
	 }
	 fout<<"Case #"<<w+1<<": "<<flag<<" ";
	fout<<retu<<"\n";
	
	}getch();
}