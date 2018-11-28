#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
int first[4][4], second[4][4];

int main() {
	ifstream cin("main.in");
	freopen("main.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 0; t < T; ++t)
	{
		int a, b;

		cin >> a;
		a--;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				cin >> first[i][j];
		cin >> b;
		b--;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				cin >> second[i][j];
		vector<int> res;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				if(first[a][i] == second[b][j])
					res.push_back(first[a][i]);
		printf("Case #%d: ", t + 1);
		if(res.size() == 0)
			puts("Volunteer cheated!");
		if(res.size() == 1)
			printf("%d\n", res[0]);
		if(res.size() > 1)
			puts("Bad magician!");
	}
	return 0;
}
