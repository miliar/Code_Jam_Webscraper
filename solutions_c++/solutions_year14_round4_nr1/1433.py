#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
#ifdef _WIN32
#include <windows.h>
#endif

using namespace std;

void solve(int index)
{
	int N, X;
	cin >> N >> X;
	vector<int> S(N);
	for (int i = 0; i < N; ++i)
	{
		cin >> S[i];
	}
	sort(S.begin(), S.end());
	int i = 0;
	int j = N - 1;
	int result = 0;
	while (j > i)
	{
		++result;
		if (S[j] + S[i] <= X)
		{
			++i;
		}
		--j;
	}

	if (i == j)
	{
		++result;
	}
	
	cout << "Case #" << index + 1 << ": ";
	cout << result;
	cout << endl;
}

int main(int argc, char **argv)
{
#ifdef _WIN32
	if (argc == 2 && string(argv[1]) == "-d")
	{
		cout << "Sleep for 10 seconds" << endl;
		Sleep(10 * 1000);
	}
#endif
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		solve(i);
	}
	return 0;
}