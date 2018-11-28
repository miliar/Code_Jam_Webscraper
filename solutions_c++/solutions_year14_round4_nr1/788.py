#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char** argv)
{
	int T;
	cin >> T;

	for(int i = 1; i <= T; i++)
	{
		int N, X;
		vector<int> files;
		cin >> N >> X;

		files.resize(N);
		for(int j = 0; j < N; j++)
		{
			cin >> files[j];
		}

		sort(files.begin(), files.end());

		int num_discs = 0;
		int head, tail;
		head = 0;
		tail = N - 1;
		while(head <= tail)
		{
			if(files[head] + files[tail] <= X)
			{
				tail--;
				head++;
			}
			else
			{
				tail--;
			}
			num_discs++;
		}
		cout << "Case #" << i << ": " << num_discs << endl;
	}
	return 0;
}

