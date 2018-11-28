#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
using namespace std;
int main(int argc, char const *argv[])
{
	int t;
	cin >> t;
	for(int j=0;j<t;j++)
	{
		long long int n,count=0,added=0;
		cin >> n;
		getchar();
		char arr[n+1];
		long long int psum[n+1];
		for (int i = 0; i<n+1; ++i)
		{
			cin >> arr[i];
			if (i==0)
			{
				psum[i]=arr[i]-48;
			}
			else
			{
				psum[i]=psum[i-1]+arr[i]-48;
			}
		}
		for (int i = 1; i < n+1 ; ++i)
		{
			int req=psum[i]+added-arr[i]+48;
			if (req<i)
			{
				added+=i-req;
			}
		}
		cout << "Case #" << j+1 << ": "<< added << endl;
	}
	return 0;
}