#include<iostream>
#include<fstream>
#include<algorithm>
#include<cstdlib>

using namespace std;

int cmp(const void *x, const void *y)
{
  double xx = *(double*)x, yy = *(double*)y;
  if (xx < yy) return -1;
  if (xx > yy) return  1;
  return 0;
}
int main()
{
	double test,n,naomi[1000],ken[1000],optimise=0,dwar=0,kenc[1000],naomic[1000];
int i,j,k=1;
	ofstream fout;
	ifstream fin; 
	fout.open("output.txt");
	fin.open("D-large(1).in");
	fin>>test;
	while(test--)
	{
		fin>>n;
		for(i=0;i<n;i++)
			fin>>naomi[i];
		for(i=0;i<n;i++)
			fin>>ken[i];
		qsort(naomi,n,sizeof(double),cmp);
		qsort(ken,n,sizeof(double),cmp);
		for(i=0;i<n;i++)
		{
			kenc[i]=ken[i];
			naomic[i]=naomi[i];
		}
		//optimised war first greater than naomi i is naomi
	
		for(i=0;i<n;i++)
		{	
			for(j=0;j<n;j++)
			{
				if((ken[j] -naomi[i])> 0 )
				{
					optimise++;

					ken[j]=-1;
					break;
				}
			}
		}
		optimise=n-optimise;
		//d war
		for(i=0;i<n;i++)
		{	
			for(j=0;j<n;j++)
			{
				if(naomi[j]>kenc[i])
				{
					dwar++;
		
					naomi[j]=-1;
					break;
					
				}
			}
		}
		for(i=0;i<1000;i++)
		{
			ken[i]=-1;
			naomi[i]=-1;
		}

		fout<<"Case"<<" "<<"#"<<k<<":"<<" "<<dwar<<" "<<optimise<<"\n";
		dwar=0;
		optimise=0;
		k++;



}
	return 0;
}