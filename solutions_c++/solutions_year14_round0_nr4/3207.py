#include <iostream>
#include <fstream>
#include <conio.h>
using namespace std;

void sort(double a[],int n)
{
	for(int i=0;i<n-1;++i)
	{
		for(int j=i+1;j<n;++j)
		{
			if(a[i]<a[j])
			{
				double t=a[i];
				a[i]=a[j];
				a[j]=t;
			}
		}
	}
}

int war(double a[],double b[],int c)
{
	int flag=0;
	
	for(int i=c-1;i>=0;--i)
	{
		for(int j=c-1;j>=0;--j)
		{
			if(b[j]>a[i])
			{
				flag++;
				a[i]=0;
				b[j]=0;
				break;
			}
		}
	}
	return flag;
}

int main()
{
	ifstream fin("D-small-attempt0.in");
	ofstream fout("output.txt");
	
	int t,i,j;
	fin>>t;
	
	for(i=0;i<t;++i)
	{
		int c,w,dw;
		
		fin>>c;
		
		double na[c],ke[c],tna[c],tke[c];
		
		for(j=0;j<c;++j)
		  fin>>na[j];
		for(j=0;j<c;++j)
		  fin>>ke[j];
		
		sort(na,c);
		sort(ke,c);
		
		for(j=0;j<c;++j)
		{
			tna[j]=na[j];
			tke[j]=ke[j];
		}
		dw=war(ke,na,c);
		w=c-war(tna,tke,c);
		
		fout<<"Case #"<<i+1<<": "<<dw<<" "<<w<<endl;
	}
	return 0;
}