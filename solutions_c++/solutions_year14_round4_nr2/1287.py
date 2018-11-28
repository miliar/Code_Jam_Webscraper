#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;

bool valid(int *arr, int size)
{
	int flag = 0;
	for(int i=0;i<size-1;i++)
	{
		if(flag == 0)
		{
			if(arr[i] < arr[i+1])
			{
				continue;
			}
			else
				flag++;
		}
		else
		{
			if(arr[i] > arr[i+1])
				continue;
			else
				return false;
		}
	}
	return true;
}
int inv_count(int *v,int *t,int size)
{
	int arr[size];
	for(int i=0;i<size;i++)
		arr[i] = v[i];
	int c = 0;
	// cout<<"arr = "<<" ";
	// for(int i=0;i<size;i++)
	// 	cout<<arr[i]<<" ";
	// cout<<endl;
	for(int i=0;i<size;i++)
	{
		int j;
		for(j = i;j<size;j++)
		{
			if(t[i] == arr[j])
			{
				break;
			}
		}
		c+= j-i;
		// cout<<t[i]<<" "<<i<<" "<<j<<endl;
		for(int k = j;k>i;k--)
		{
			arr[k] = arr[k-1];
		}
		// cout<<"after : ";
		// for(int k=0;k<size;k++)
		// 	cout<<arr[i]<<" ";
		// cout<<endl;
		// arr[i] = t[i];
	}
	return c;
}
int main()
{
  int T;
  cin>>T;
  for(int _t=1;_t<=T;_t++)
  {
  	int n;
  	cin>>n;
  	int a;
  	// vector<int> v;
  	int v[20],t[20];
  	for(int i=0;i<n;i++)
  	{
  		cin>>a;
  		v[i] = a;
  		t[i] = a;
  	}
  	sort(t,t+n);
  	int m = 1e7;
  	do{
  		if(valid(t,n))
  		{
  			int c = inv_count(v,t,n);
  			if(c < m)
  				m = c;
  			// cout<<c<<endl;
  			// for(int i=0;i<n;i++)
  			// 	cout<<t[i]<<" ";
  			// cout<<endl;
  		}
  	}while(next_permutation(t,t+n));
  	cout<<"Case #"<<_t<<": "<<m<<endl;
  }
}