//Google Codejam
//2013 Qualification Round
//Alan Richards - alarobric

//Problem B
#include <sstream>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <map>
using namespace std;

#define FOR(i, n) for(int i=0; i<n; i++)
#define FOREACH(c, iter) for(auto iter=c.begin(); iter!=c.end(); iter++)

vector<int> arrM;

string Solve(int i_case)
{
	int N, M;
	std::cin >> N >> M;
	vector<vector<int>> plan;
	//int plan[N][M] = {0};
	int maxInRow[N];
	int maxInCol[M];
	FOR(i,N)
		maxInRow[i] = 0;
	FOR(i, M)
		maxInCol[i] = 0;
	FOR(i, N)
	{
		vector<int> row;
		FOR(j, M)
		{
			int in;
			cin >> in;
			row.push_back(in);
			if (in > maxInRow[i])
				maxInRow[i] = in;
			if (in > maxInCol[j])
				maxInCol[j] = in;
		}
		plan.push_back(row);
	}
	
	//check each square - if something in it's row is higher, and something in its column is higher, then fail
	FOR(i,N)
		FOR(j,M)
		{
			if ((maxInRow[i] > plan[i][j]) && (maxInCol[j] > plan[i][j]))
				return "NO";
		}
	
	return "YES";
}

int main()
{
	std::cerr << "GCJ Practice" << std::endl;
	int numCases;
	std::cin >> numCases;
	for (int i=1; i<=numCases; i++)
	{
		std::cout << "Case #" << i << ": " << Solve(i) << std::endl;
	}
	return 0;
}