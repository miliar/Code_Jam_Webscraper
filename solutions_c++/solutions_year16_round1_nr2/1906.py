#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long ll;



int main()
{
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	//freopen("A.in","r",stdin);freopen("A.out","w",stdout);
	int testcase;

	int N[50][50];
	int NB[100][50];
	int H[2501];


	scanf("%d", &testcase);
	for (int case_id = 1; case_id <= testcase; case_id++)
	{
		for (int i = 0; i < 50;i++)
		for (int j = 0; j < 50; j++)
		{
			N[i][j] = 0;
			NB[i][j] = 0;
		}
		memset(H, 0, sizeof(int)* 2501);
		int n;
		printf("Case #%d: ", case_id);
		cin >> n;
		for (int i = 0; i < 2*n-1; i++)
		for (int j = 0; j < n; j++)
		{
			int tmp;
			cin >> tmp;
			H[tmp]++;
		}
		vector<int> r;
		for (int i = 1; i < 2501;i++)
		if (H[i] % 2 == 1) r.push_back(i);
		sort(r.begin(), r.end());
		for (int i = 0; i < r.size(); i++)
			cout << r[i] << " ";
		
		printf("\n");
	}
	return 0;
}

