#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Party
{
	int index;
	int members;
};

int main(int argc, char** argv)
{
	ios::sync_with_stdio(false);
	//cin.tie(nullptr);

	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		int N;
		cin >> N;

		int S = 0, P = N;
		vector<Party> parties(N);
		for (int i = 0; i < N; ++i)
		{
			parties[i].index = i;
			cin >> parties[i].members;
			S += parties[i].members;
		}

		auto comp = [](const Party& a, const Party& b) {
			return a.members > b.members;
		};

		cout << "Case #" << t << ": ";
		do {
			sort(parties.begin(), parties.end(), comp);
			if (P > 3)
			{
				cout << (char)('A' + parties[0].index) << (char)('A' + parties[1].index) << ' ';
				--parties[0].members;
				--parties[1].members;
				if (parties[0].members == 0) --P;
				if (parties[1].members == 0) --P;
				S -= 2;
			} else if (P == 3)
			{
				cout << (char)('A' + parties[0].index) << ' ';
				--parties[0].members;
				if (parties[0].members == 0) --P;
				--S;
			} else if (P == 2)
			{
				if (parties[0].members == parties[1].members)
				{
					cout << (char)('A' + parties[0].index) << (char)('A' + parties[1].index) << ' ';
					--parties[0].members;
					--parties[1].members;
					if (parties[0].members == 0) --P;
					if (parties[1].members == 0) --P;
					S -= 2;
				} else
				{
					cout << (char)('A' + parties[0].index) << ' ';
					--parties[0].members;
					if (parties[0].members == 0) --P;
					--S;
				}
			}
		} while (S > 0);

		cout << '\n';
	}

	return 0;
}
