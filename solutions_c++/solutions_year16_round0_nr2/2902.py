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

void work(ll testCase)
{
	string s;
	cin >> s;
	vector<bool> arr(s.size(),false);
	for (int i = 0; i < arr.size(); ++i)
	{
		if (s[i] == '+')
			arr[i] = true;
	}
	int last = arr.size() - 1;
	int c = 0;
	while (find(arr.begin(), arr.end(), false) != arr.end())
	{
		while (arr[last] == 1)
			--last;
		for (int i = 0; i <= last; ++i)
			arr[i] = !arr[i];
		++c;
	}
	file<<"Case #"<<testCase<<": "<< c << endl;
}
int main()
{
	file.open("p2.txt");

	int n;
	cin >> n;
	for (int i = 1; i <= n;++i)
	{
		work(i);
	}
}