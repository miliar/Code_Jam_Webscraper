#include <cstdio>
#include <utility>
#include <algorithm>
#include <vector>
#include <set>

#define mp make_pair
#define point pair<int, int> 
#define px first
#define py second
#define INF 100000000
#define EPS 1e-9
#define rint(x) scanf("%d", &(x))
#define loop(i, x) for (int i = 0; i < (x); i++)

using namespace std;

int getrow(int num, int board[4][4])
{
	loop(i, 4)
		loop(j, 4)
			if (board[i][j] == num)
				return j+1;
}

bool poss(int num, int ans1, int board1[4][4], int ans2, int board2[4][4])
{
	return getrow(num, board1) == ans1 && getrow(num, board2) == ans2;
}

int main()
{
	const int S = 4;
	
	int cases;
	rint(cases);
	
	loop(testcase, cases)
	{
		int board1[S][S];
		int board2[S][S];
		
		int ans1;
		rint(ans1);
		loop(j, S)
			loop(i, S)
				rint(board1[i][j]);
		
		int ans2;
		rint(ans2);
		loop(j, S)
			loop(i, S)
				rint(board2[i][j]);
		
		vector<int> V;
		loop(num, 16)
			if (poss(num+1, ans1, board1, ans2, board2))
				V.push_back(num+1);
		
		if (V.size() == 0)
			printf("Case #%d: Volunteer cheated!\n", testcase+1);
		else if (V.size() > 1)
			printf("Case #%d: Bad magician!\n", testcase+1);
		else
			printf("Case #%d: %d\n", testcase+1, V[0]);
	}
}