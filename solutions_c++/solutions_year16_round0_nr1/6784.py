#include<iostream>
#include<stdlib.h>
#include<fstream>
#include<string>
#include<map>
#include<vector>
#include<list>
#include<queue>
#include<algorithm>
#include<limits>
#include<time.h>
using namespace std;

int main()
{
	int T;
	long a[101],ans[101];
	cin>>T;
	for(int i=0;i<T;i++)
		cin>>a[i];
	for(int i=0;i<T;i++)
	{
		map<int,int> nums;
		long j = 1;
		long last=-1;
		if(a[i] != 0)
		{
			while(nums.size()!=10)
			{
				long test = j*a[i];
				last = test;
				while(test!=0)
				{
					if(nums.find(test%10) ==nums.end())
						nums[test%10] = 1;
					test = test/10;
				}
				j++;
			}
		}
		ans[i] = last;
	}
	for(int i=0;i<T;i++)
		ans[i] == -1? cout<<"Case #"<<i+1<<": "<<"INSOMNIA\n":cout<<"Case #"<<i+1<<": "<<ans[i]<<"\n";
	return 0;
}