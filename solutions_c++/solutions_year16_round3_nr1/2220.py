#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

bool valid(vector<int> &nums, int n, int sum)
{
	for (int i = 0; i < n; ++i)
	{
		if (nums[i] > sum / 2) return false;
	}
	return true;
}

string getS(vector<int> &nums, int n, int sum)
{
	string ret;
	if (n == 2)
	{
		for (int i = 0; i < nums[0]; ++i)
			ret += " AB";
		return ret;
	}

	bool flag = true;
	while (1)
	{
		flag = true;
		for (int i = 0; i < n; ++i)
		{
			if (nums[i] == 0) continue;
			flag = false;
			if (nums[i] >= 2)
			{
				nums[i] -= 2; sum -= 2;
				if (valid(nums, n, sum))
				{
					ret += " ";
					ret += ('A' + i);
					ret += ('A' + i);
					break;
				}
				nums[i] += 2; sum += 2;
			}
			if (nums[i] == 1)
			{
				nums[i] -= 1; sum -= 1;
				if (valid(nums, n, sum))
				{
					ret += " ";
					ret += ('A' + i);
					break;
				}
				nums[i] += 1; sum += 1;
			}
			nums[i] -= 1; sum -= 2;
			bool f = false;
			for (int j = i; j < n; ++j)
			{
				if (nums[j] == 0) continue;
				nums[j] -= 1;
				if (valid(nums, n, sum))
				{
					ret += " ";
					ret += ('A' + i);
					ret += ('A' + j);
					f = true;
					break;
				}
				nums[j] += 1;
			}
			if (!f)
			{
				nums[i] += 1; sum += 2;
			}
		}
		if (flag) break;
	}
	return ret;
}

int main()
{
	//freopen("C:/Users/tcwg-ljb/Desktop/in.in", "r", stdin);
	//freopen("C:/Users/tcwg-ljb/Desktop/out.txt", "w", stdout);
	freopen("C:/Users/tcwg-ljb/Desktop/large.in", "r", stdin);
	freopen("C:/Users/tcwg-ljb/Desktop/largeout.txt", "w", stdout);
	int cas;
	cin >> cas;
	int j = 1;
	//t << ('A' + 1) << endl;
	while (cas)
	{
		int n;
		cin >> n;
		vector<int> nums(n);
		int sum = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> nums[i];
			sum += nums[i];
		}
		cout << "Case #" << j++ << ":" << getS(nums, n, sum) << endl;
		cas--;
	}
	return 0;
}