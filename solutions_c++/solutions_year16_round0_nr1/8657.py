#include <iostream> 
#include <cstdio> 
#include <vector>
#include <algorithm>
using namespace std;
void decomp(int n,vector<int>&nums)
{
	while (n > 0)
	{
		bool k = true;
		int a = n % 10;
		for (size_t i = 0; i < nums.size(); i++)
		{
			if (nums[i] == a)
			{
				k = false;
			}
		}
		if (k == true){ nums.push_back(a); }
		n /= 10;
	}
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (size_t i = 0; i < t; i++)
	{   
		vector<int>nums(0);
		int n;
		cin >> n;
		int y = n;
		if (n == 0){ cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl; }
		else 
		{
			while (nums.size() <10)
			{
				decomp(n, nums);
				n += y;
			}
			cout << "Case #"<<i+1<<": "<<n - y << endl;
		}
	}
}