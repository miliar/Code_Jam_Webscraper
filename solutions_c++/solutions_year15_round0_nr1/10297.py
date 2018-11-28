#include<bits/stdc++.h>
using namespace std;

int main()
{
	ifstream file1;
	ofstream file2;
	int tc;
	file1.open("inp.txt");
	file2.open("outp.txt");
	file1>>tc;
	//cin>>tc;
	for(int k = 1; k <= tc; k++)
	{
		int smax;
		//cin>>smax;
		file1>>smax;
		string arr;
		//cin>>arr;
		file1>>arr;

		long long int sum = 0, req = 0;
		for(int i = 0; i <= smax; i++)
		{
			if(arr[i] == '0')
			{
				continue;
			}
			else
			{
				if(i > sum)
				{
					req += (i-sum);
					sum += (req + (arr[i]-'0'));
				}
				else
				{
					sum += (arr[i]-'0');
				}
			}
		}
		//cout<<req<<endl;
		file2<<"Case #"<<k<<": "<<req<<endl;
	}
}
