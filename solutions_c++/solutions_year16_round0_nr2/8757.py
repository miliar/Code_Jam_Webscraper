#include <iostream> 
#include <cstdio> 
#include <vector>
#include <string>
using namespace std;
void revers(string &p, int i)
{
	for (size_t j = 0; j <=i; j++)
	{
		if (p[j] == '+'){ p[j] = '-'; }
		else if (p[j] == '-'){ p[j] = '+'; }
	}
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (size_t i = 0; i < T; i++)
	{
		string pancake;
		long long sum=0;
		cin >> pancake;
		int j = pancake.size() - 1;
		while (pancake.size()!= 0)
		{
			if (pancake[j] == '-')
			{
				revers(pancake, j);
				sum++;
			}
			j--;
			pancake.pop_back();
		}
		cout << "Case #" << i+1<< ": " << sum << endl;
	}
}