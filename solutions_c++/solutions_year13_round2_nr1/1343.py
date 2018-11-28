#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>
using namespace std ;
typedef unsigned long long LL ;
LL sz[100];
int N;
int rec(int i, LL s)
{
	if(i == N)
		return 0;
	int ans;
	if(s > sz[i])
		ans = rec(i + 1, s + sz[i]);
	else
	{
		if(s == 1)
			ans = rec(N, s) + N - i;
		else
			ans = min(rec(i, s + s - 1) + 1, rec(N, s) + N - i);
	}
	return ans;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt", "w", stdout);
	LL T, A;
	cin >> T;
	for(int ti = 1; ti <= T; ++ti)
	{
		cin >> A >> N;
		for(int i = 0; i < N; ++i)
			cin >> sz[i];
		sort(sz, sz + N);
		cout << "Case #" << ti << ": " << rec(0, A) << endl;
	}
}