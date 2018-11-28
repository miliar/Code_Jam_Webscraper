#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<math.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	int i,j;
	int arr[1];
	string s;
	int sum ,sh=0;
	int shit;
	for (i = 0; i <n; i++)
	{
		cin>>arr[0];
		cin>>s;
		sum=0;
		shit=0;
		for (j = 0; j <= arr[0]; j++)
		{
			if (sum<j)
			{
				shit += j-sum;
				sum = j;
			}
			
			else
			{

			}

			sum = sum + s[j]-'0';

			
			

		}
	
		cout<<"Case #"<<i+1<<": "<<shit;
	cout<<"\n";
	}



}
