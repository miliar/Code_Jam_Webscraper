#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#pragma warning (disable:4996)
using namespace std;

int main()
{
	int T;
	vector<unsigned long long> nums;
	freopen("D:\\C-large-1.in","r",stdin);
	freopen("D:\\C-large-1.out","w",stdout);
	ifstream ifs;
	ifs.open("D:\\2.txt");
	for(int i=0;i<39;++i)
	{
		unsigned long long k;
		ifs>>k;
		nums.push_back(k);
	}
	ifs.close();
	cin>>T;
	for(int i=1;i<=T;++i)
	{
		unsigned long long left,right;
		cin>>left>>right;
		int rez=0;
		for(int j=0;j<nums.size();++j)
			if(nums[j]<=right && nums[j]>=left)
				++rez;
		cout<<"Case #"<<i<<": "<<rez<<endl;
	}
	return 0;
}
