#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution
{
public:
	void getSolution(int i,int k,int c,int s)
	{
		cout << "Case #" << i + 1 << ": 1";
		for (int i = 2; i <= s; ++i)
			cout << " " << i;
		cout << endl;
	}

};

int main()
{
	//freopen("C:/Users/ywy/Desktop/large.in", "r", stdin);
	//freopen("C:/Users/ywy/Desktop/large-out.txt", "w", stdout);
	freopen("C:/Users/ywy/Desktop/in.in", "r", stdin);
	freopen("C:/Users/ywy/Desktop/out.txt", "w", stdout);
	int n;
	cin >> n;
	Solution ss;
	for (int i = 0; i < n; ++i)
	{
		int k, c, s;
		cin >> k >> c >> s;
		ss.getSolution(i, k, c, s);
	}
	return 0;
}