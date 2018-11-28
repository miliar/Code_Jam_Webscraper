#include <iostream>
#include <algorithm>
#include <map>     
#include <vector>
using namespace std;

int ans1, ans2;
int board1[4][4], board2[4][4];

void scan_board(int board[4][4])
{
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			scanf("%d", &board[i][j]);
}

void solve()
{
	scanf("%d", &ans1);
	ans1--;
	scan_board(board1);
	scanf("%d", &ans2);
	ans2--;
	scan_board(board2);

	map<int, int> cnt;
	for (int i = 0; i < 4; i++)
		cnt[board1[ans1][i]]++;
	for (int i = 0; i < 4; i++)
		cnt[board2[ans2][i]]++;

	vector<int> good;
	for (auto it = cnt.begin(); it != cnt.end(); it++)
		if (it->second > 1)
			good.push_back(it->first);

	if (good.size() == 1)
		printf("%d\n", good[0]);
	else if (good.size() == 0)
		printf("Volunteer cheated!\n");
	else
		printf("Bad magician!\n");	
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}

	return 0;	
}