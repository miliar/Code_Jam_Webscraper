#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
ifstream inFile ("2015QB.in");
ofstream outFile ("2015QB.out");

void solve() {
	int D;
	inFile >> D;
	vector<int> P;
	for (int i = 0; i < D; ++i)
	{
		int temp;
		inFile >> temp;
		P.push_back(temp);
	}
	sort(P.begin(), P.end(), greater<int>());
	int ans = P.front();
	for (int waitTime = 2; waitTime < P.front(); ++waitTime)
	{
		int total = waitTime;
		for (auto i = P.begin(); i != P.end() && *i > waitTime; ++i)
			total += (*i+waitTime-1)/waitTime - 1;
		ans = min(ans, total);
	}
	outFile << ans;
}

int main(int argc, char const *argv[])
{
	
	// inFile.open("2015QB.in");
	// outFile.open("2015QB.out");

	int T;
	inFile >> T;
	for (int i = 0; i < T; ++i)
	{
		outFile << "Case #" << i+1 << ": ";
		solve();
		outFile << endl;
	}

	outFile.close();
	inFile.close();
	return 0;
}
