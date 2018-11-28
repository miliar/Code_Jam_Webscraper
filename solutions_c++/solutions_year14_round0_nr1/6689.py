#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <stdio.h>
#include <iomanip>

using namespace std;

int arr[4][4];

void intersection(int* arr1,int* arr2);

int main()
{
	int t,i=0;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		int j=0,u1,u2,k,l=0;
		int *arru1,*arru2;
		cin>>u1;

		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>arr[j][k];
			}
		}
		arru1 = new int[4];
		for(l=0;l<4;l++)
			arru1[l]=arr[u1-1][l];
			
		cin>>u2;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>arr[j][k];
			}
		}
		arru2 = new int[4];
		for(l=0;l<4;l++)
			arru2[l]=arr[u2-1][l];
			
		sort(arru1,arru1+4);
		sort(arru2,arru2+4);
		cout<<"Case #"<<i<<": ";
		intersection(arru1,arru2);
		cout<<endl;
	}
}

void intersection(int* arr1,int* arr2)
{
	int i = 0, j = 0,size=0,res;
	while(i < 4 && j < 4)
	{
		if(arr1[i] < arr2[j])
		i++;
		else if(arr2[j] < arr1[i])
		j++;
		else /* if arr1[i] == arr2[j] */
		{
			res = arr2[j++];
			size++;
			i++;
		}
	}
	if(size==1)
	{cout<<res;}
	else if(size==0)
	{cout<<"Volunteer cheated!";}
	else
	{cout<<"Bad magician!";}
}
