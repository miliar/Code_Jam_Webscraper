#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <deque>

using namespace std;

int main (int argc, char* argv[])
{
	int T;
	cin >> T;
	for (int cas = 1; cas < T+1; cas += 1)
	{
		cout << "Case #" << cas << ": ";
		int res = 0;
		vector<int> files;
		int N, M;
		cin >> N >> M;
		int temp;
		for (int i = 0; i < N; i += 1)
		{
			cin >> temp;
			files.push_back(temp);
		}
		sort (files.begin(),files.end());
		
		vector<bool> used;
		for (int i = 0; i < N; i += 1)
		{
			used.push_back(false);
		}
		for (int i = 0; i < N; i += 1)
		{
			if (used[i]) continue;
			used[i] = true;
			for (int j = N-1; j >=0; j -= 1)
			{
				if (!(used[j]) and files[i] + files[j] <= M)
				{
					used[j] = true;
					break;
				}
			}
			res++;
		}
		cout << res << endl;
	}
	return 0;
}
