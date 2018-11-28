#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
 ifstream inP("q.in");
 ofstream outP("q2.txt");
	int Tem,v1,v2,ind1=0,ind2=0;
	inP>>Tem;
	for(int i=1;i<=Tem;i++)
	{
	inP>>v1;
	inP>>v2;
	int arr1[v1][v2];
	int arr2[v1][v2];
	for(int j=0;j<v1;j++)
	 for(int k=0;k<v2;k++)
		inP>>arr1[j][k];
	for(int j=0;j<v1;j++)
	 for(int k=0;k<v2;k++)
		arr2[j][k]=2;
///******************************************************************************************
	int a1,a2;
	
	for(int j=0;j<v1;j++)
	{
		for(int k=0;k<v2;k++)		
		if(arr1[j][k]==1)
		{
			ind1=0,ind2=0;
			 a1=j;
			 a2=k;
			for(int r=0;r<v2;r++)
			 if(arr1[a1][r]!=1)
			 {
			 ind1=1;
			 break;
			 }
			for(int r=0;r<v1;r++)
			 if(arr1[r][a2]!=1)
			 {
			 ind2=1;
			 break;
			 } 
			 
			 if(ind1==0)
			for(int r=0;r<v2;r++)
			arr2[a1][r]=1;
			if(ind2==0)
			for(int r=0;r<v1;r++)
			arr2[r][a2]=1;	
		}
		}
		int count1=0;
	for(int j=0;j<v1;j++)
	{
		for(int k=0;k<v2;k++)
		{
	 		if(arr1[j][k]!=arr2[j][k])
				{
				count1=1;
				break;
				}
	   }

	}
 	
	if(count1==0)
	outP<<"Case #"<<i<<": YES"<<endl;
	else
	outP<<"Case #"<<i<<": NO"<<endl;			
	}
}
