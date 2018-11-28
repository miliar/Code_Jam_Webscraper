#include <iostream>
#include <algorithm>
using namespace std;

int n_opp(int* motes, int n, int a)
{
	if (a <= 1 && motes[0] >= a)
	{
		return n;
	}
	
	for (int i = 0; i < n; i++)
	{
		if (motes[i] < a)
		{
			a += motes[i];
		}
		else
		{
			return min(
					n_opp(motes + i, n - i, a + a - 1),
					n_opp(motes + (i + 1), n - (i + 1), a)
				) + 1;
		}
	}
	return 0;
}
 
int main(int argc, char** argv) {
	int t;
	/*long long*/ unsigned int a;
	int n;
	int motes[100];
	int result;
	
	cin >> t;
	for (int testcase = 1; testcase <= t; testcase++)
	{
		cin >> a;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> motes[i];
		}
		
		sort(motes, motes + n);
		cout << "Case #" << testcase << ": " << n_opp(motes, n, a) << endl;
	}
	return 0;
}

