#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <list>
#include <stack>
#include <functional>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
  
	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t)
	{
		int n;
		cin >> n;
		vector<int> A(n);
		vector<int> B(n);
		set<pair<int, int>> S;
		for(int i = 0; i < n; ++i)
		{
			cin >> A[i];
			S.insert(make_pair(A[i], i));
		}

		int cur = 0;
		for(auto val: S)
			B[val.second] = cur++;

		//for(int i = 0; i < n; ++i)
		//	cout << B[i] << " ";
		//cout << endl;

		int ans = 0;
		int l = 0, r = 0;
		for(int i = 0; i < n; ++i)
		{
			for(int j = l; j < n - r; ++j)
			{
				if(B[j] == i)
				{
					if(j - l < n - r - j - 1)
					{
						int sv = B[j];
						for(int k = j; k > l; --k)
							B[k] = B[k-1];
						B[l] = sv;
						ans += j - l;
						++l;
					}
					else
					{
						int sv = B[j];
						for(int k = j; k < n - r - 1; ++k)
							B[k] = B[k+1];
						B[n - r - 1] = sv;
						ans +=  n - r - j - 1;
						++r;
					}
					break;
				}
			}
		}

		cout << "Case #" << t << ": " << ans << endl;
	}

    return 0;
}