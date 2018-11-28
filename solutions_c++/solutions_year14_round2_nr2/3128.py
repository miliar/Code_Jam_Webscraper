#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>

using namespace std;

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for (int qq = 1; qq <= tt; qq++) 
	{
		long long A, B, K;
		int count = 0;
		printf("Case #%d: ", qq);
		cin >> A >> B >> K;
		for (int i = 0; i < A; i++)
		{
			for (int j = 0; j < B; j++)
			{
				if ((i & j) < K)
					++count;
			}
		}
		cout << count << endl;
		
	}
	return 0;
}
