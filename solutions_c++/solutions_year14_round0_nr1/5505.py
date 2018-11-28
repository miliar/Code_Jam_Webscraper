#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

vector<int> inter(vector<int> list1, vector<int> list2)
{
	sort(list1.begin(), list1.end());
	sort(list2.begin(), list2.end());
 	vector<int> list(max(list1.size(), list2.size()));
 	int t = set_intersection(list1.begin(), list1.end(), list2.begin(), list2.end(), list.begin()) - list.begin();
 	list.resize(t);
 	return list;
}

vector<int> read_row()
{
	vector<int> list(4);
 	for (int i = 0; i < 4; i++)
 		scanf("%d", &list[i]);
 	return list;
}

vector<int> mx1[4], mx2[4];

void solve()
{
	int r1;
	scanf("%d", &r1); r1--;

	for (int i = 0; i < 4; i++)
		mx1[i] = read_row();

	int r2;
	scanf("%d", &r2); r2--;

	for (int i = 0; i < 4; i++)
		mx2[i] = read_row();
	
	vector<int> res = inter(mx1[r1], mx2[r2]);
	if (res.empty())
		cout << "Volunteer cheated!" << endl;
	else if (res.size() != 1)
		cout << "Bad magician!" << endl;
	else
		cout << res[0] << endl; 
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif

	int it;
	cin >> it;
	for (int i = 1; i <= it; i++)
	{
	 	printf("Case #%d: ", i);
	 	solve();
	}

 	return 0;
}