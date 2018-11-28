/*************************************************************************
    > File Name: A.cpp
    > Author: wmg_1007
    > Mail: wmg_1007@163.com
    > Created Time: 2017年04月08日 星期六 21时50分36秒
 ************************************************************************/

#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <iomanip>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <deque>
using namespace std;

string S;
int n, K;

void ReverseS(int st)
{
	for (int i = st; i < st + K; i++)
		if (S[i] == '-')
			S[i] = '+';
		else
			S[i] = '-';
}

int main()
{
	int T, caseT = 0;
	cin >> T;
	while (T--) {
		cin >> S;
		while (S[0] != '-' && S[0] != '+')
			cin >> S;
		cin >> K;
		n = S.size();
		int ans = 0;
		for (int i = 0; i < n - K + 1; i++) 
			if (S[i] == '-') { 
				ReverseS(i);
				ans++;
			}
		for (int i = n - K + 1; i < n; i++)
			if (S[i] == '-')
				ans = -1;
		cout << "Case #" << ++caseT << ": ";
		if (ans == -1)
			puts("IMPOSSIBLE");
		else
			cout << ans << endl;
	}
	return 0;
}



		
