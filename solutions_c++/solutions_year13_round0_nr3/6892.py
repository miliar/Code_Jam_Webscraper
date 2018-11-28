#include<iostream>
#include <stdio.h>
#include <math.h>
using namespace std;



int maxfunction(int start,int end,int size,int arr[])
{
	if(size<=2)
	{
		int max=0;
		if(arr[start]>arr[end])
		{
			max=arr[start];
		}
		else
		{
			max=arr[end];
		}			
			return max;
	}

	else
	{
		int half=(size/2);

		int leftarrmax=maxfunction(start,start+half-1,half,arr);
		int rightarrmax=maxfunction(start+half,end,half,arr);
			
		if(leftarrmax>rightarrmax)
		{
			return leftarrmax;
		}
		else{
			return rightarrmax;
		}
		}
		
}
void main()
{
	cout << "the array is : ";
	int arr[20]; for(int i=0; i<20; i++) {arr[i]=(rand()%1000)+1; cout << arr[i] << " "; }

	int x=maxfunction(0,19,20,arr);// starting index, last index, array, total elements

	cout<<"maximum number is: "<<x<<endl;

	system("pause");
}