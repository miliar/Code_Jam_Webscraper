// This file was compiled using clang-503.0.40
// clang++ -o run.bin -std=c++11 task.cxx
// ./run.bin < data.in > data.out

# include <iostream>
# include <string>
# include <sstream>
# include <iomanip>

# include <algorithm>
# include <vector>
# include <map>
# include <set>
# include <queue>
# include <deque>
# include <stack>
# include <bitset>

# include <cstdio>
# include <cstdlib>
# include <ctime>
# include <climits>
# include <limits>
# include <cstring>
# include <cmath>

using namespace std;

int main()
{
	int T_inp; cin >> T_inp;
	for(int T=1; T<=T_inp; ++T)
	{
		int N, X; cin >> N >> X;
		
		vector<int> vec(N);
		for(int i=0; i<vec.size(); ++i) cin >> vec[i];
		
		sort(vec.begin(), vec.end());
		
		int ans = 0;
		
		int left = 0, right = vec.size() -1;
		while(left <= right)
		{
			if (left == right)
			{
				ans += 1;
				break;
			}
			else 
			{
				if (vec[left] + vec[right] <= X)
				{
					++ans;
					++left, --right;
				}
				else 
				{
					++ans;
					--right;
				}
			}
		}
		
		printf("Case #%d: %d\n", T, ans);
	}
	return 0;
}