#include <cmath>
#include <cstdio>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <iomanip>
#include <locale>
#include <sstream>
using namespace std;

int sumArray(int arr[10])
{
	int sum = 0;
	for(int i = 0;i<10;i++)
	{
		sum+=arr[i];
	}
	return sum;
}

int main()
{
	int t = 0;
	vector<int> input;
	long long int N = 0,temp = 0,times = 1;
	int arr[10] = {};
	cin >> t;
	for(int i = 0 ; i<t ;i++)
	{ 
		N = 0;
		cin >> N;
		input.push_back(N);
	}
	for(int i = 0 ; i<t ;i++)
	{ 
		N = input[i];
		times = 1;
		temp = N;
		string testCase = static_cast<ostringstream*>( &(ostringstream() << (i+1)) )->str();
		memset(arr, 0, sizeof(arr));
		while(sumArray(arr) != 10)
		{
			temp = N*times;
			//cout<<"value is"<<temp<<endl;
			if(temp <=0)
				{
					string str = "Case #"+testCase+": "+"INSOMNIA";
					cout << str<<endl;
					break;
				}

			while(temp>0)
			{
				//cout<<"inside loop for value" << temp;
				arr[temp%10] = 1;
				temp = temp/10;	
			}
			times++;	
		}
		if(sumArray(arr)== 10)
		{
			
			long long int ans = N*(times-1);
			string number = static_cast<ostringstream*>( &(ostringstream() << ans) )->str();
			string str = "Case #"+testCase+": "+number;
			cout << str <<endl;
		}
		
	}
	
}
