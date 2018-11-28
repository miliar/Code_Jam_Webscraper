#include <fstream>
#include <string>
#include <vector>
using namespace std;
int main()
{
	ifstream cin("B-small-attempt0.in");
	ofstream cout("output.txt");

	int t;
	cin >> t;
	for (int l = 1; l <= t; ++l)
	{
		int a, b, k;
		cin >> a >> b >> k;
		
		int tmp;
		long long count = 0;
		for (int i = 0; i < a; ++i)
		{
			for (int j = 0; j < b; ++j)
			{
				tmp = i&j;
				if(tmp < k)
					++count;
			}
		}
		cout << "Case #" << l << ": " << count <<endl;
	}
}