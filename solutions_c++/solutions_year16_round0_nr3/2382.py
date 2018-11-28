#include <algorithm>
#include <tuple>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;
using ll = unsigned long long;

int table[(1 << 10)+1];
int ssize;
int nmm = numeric_limits<int>::max() / 2048;
int ans;
ofstream file;
ll devisiorOf(ll num)
{
	auto j = sqrt(num) + 1;
	for (ll i = 2; i <= j; ++i)
	{
		if ((num % i) == 0)
			return i;
	}
	return num;
}
ll stoi(string s, int radix)
{
	ll ret = 0;
	int ssize = s.size();
	for (int i = 0; i < ssize; ++i)
	{
		ret *= radix;
		if (s[i] == '1')
			ret += 1;
	}
	return ret;
}
void work(int x,int y)
{
	int val = (1<<x-1) + 1;

	int temp = 0;
	while (val < (1 <<x))
	{
		++val;
		vector<int> arr;
		char buffer[1024] = { 0, };
		if (val % 2 == 0)continue;
		itoa(val, buffer, 2);
		for (int radix = 2; radix <= 10; ++radix)
		{
			string s = buffer;
			//auto j = stoi(s, 0, radix);
			auto j = stoi(s, radix);
			auto k = devisiorOf(j);
			if (k == j)
			{
				break;
			}
			else
			{
				arr.push_back(k);
			}
		}
		if (arr.size() == 9)
		{
			++temp;
			file << buffer << ' ';
			for (auto q : arr)
				file << q << ' ';
			file << endl;
			if (temp == y)
				return;
		}
	}
}
int main()
{
	int t;
	cin >> t;
	int x, y;
	cin >> x >> y;
	file.open("p2.txt");
	file << "Case #1:" << endl;
	work(x,y);
	//string s = "1001";
	//for (int i = 2; i <= 10; ++i)
	//	cout << stoi(s, i) << endl;
}