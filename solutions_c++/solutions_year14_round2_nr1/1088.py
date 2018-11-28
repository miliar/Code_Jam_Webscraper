#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;

int minn (vector<int>& L)
{
	int S = L.size();
	int minc = 1234557;

	for(int t = 0; t <= 200; ++t)
	{
		int sum = 0;
		for(int i = 0; i < S; ++i) sum += abs(t - L[i]);
		if (sum < minc) minc = sum;
	}
	return minc;
}

bool Eq(string A, string B)
{
	if (A.length() != B.length())return false;
	for(int i = 0; i<A.length(); ++i)if (A[i] != B[i]) return false;
	return true;
}

void Solving(int test)
{
	int N;
	cin >> N;
	int ans = 0;

	vector<string> Str(N);
	for(int i = 0; i<N; ++i){cin>>Str[i];}

	vector<string>shorts(N);
	vector<vector<int> >nums(N);

	for(int i = 0; i<N; ++i)
	{
		for(int j = 0; j<Str[i].size(); ++j)
			{
				if (j == 0 || Str[i][j - 1] != Str[i][j]){shorts[i].push_back(Str[i][j]); nums[i].push_back(1);} 
				else 
					nums[i][nums[i].size() - 1]++;
			}
	}

		for(int i = 0; i<N; ++i)cerr << shorts[i] << "\n";

		for(int i = 0; i<N - 1; ++i)if (!Eq(shorts[i], shorts[i + 1])){cout << "Case #" << test <<": Fegla Won\n"; return;}

		for(int i = 0; i<shorts[0].size(); ++i)
		{
			vector<int>column;
			for(int j = 0; j<N; ++j)column.push_back(nums[j][i]);
			ans += minn(column);
		}
		cout << "Case #" << test <<": " << ans << "\n";
		
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;

	for(int i = 1; i<= T; ++i)
	{
		Solving(i);
	}

	

}