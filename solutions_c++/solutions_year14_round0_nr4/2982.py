#include<iostream>
using namespace std;
#include<stdio.h>
#include <fstream>
ofstream outf("output.txt");
ifstream inf("D-small-attempt0.in");
void sort(double arr[],int n)
{
	double temp;
	for(int i = 0; i<n-1; i++)
	{
		for(int j=i; j<n; j++)
		{
			if(arr[j]>arr[i])
			{
				temp=arr[j];
				arr[j]=arr[i];
				arr[i]=temp;
			}
		}
	}
}

int main()
{	
	int t =0 ;	
	inf >> t;
	for(int i = 0; i <t ; i++)
	{
		int count =0,war=0,dwar=0;	
		inf>>count;
		double naomi[count], ken[count],tk[count],tn[count];
		for(int j=0;j<count; j++)
					inf>>naomi[j];
		for(int j=0;j<count; j++)
					inf>>ken[j];			
			
	sort(ken,count);
	sort(naomi,count);	
	
	for(int p = 0; p<count; p++)
	{
		tk[p]=ken[p];
		tn[p]=naomi[p];
	}
	
	for(int i=count-1;i>=0;i--)//kens array
	{
		for(int j=count-1; j>=0; j--)//naomis array
		{
			if(tn[j]>tk[i])
			{
				dwar++;	
				tn[j]=0;tk[i]=0;
				break;			
			}
		}
	}	
	//finding war
	for(int i=count-1;i>=0;i--)//kens array
	{
		for(int j=count-1; j>=0; j--)//naomis array
		{
			if(ken[j]>naomi[i])
			{
				war++;	
				ken[j]=0;naomi[i]=0;
				break;			
			}
		}
	}
	war = count - war;
	outf<<"Case #"<<i<<": "<<dwar<<" "<<war<<"\n";
	}
		return 0;
}
		
				