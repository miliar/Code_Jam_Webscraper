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

void make_short(vector<int8_t> &shr, vector<int> &vec)
{
	vector<int> ord(vec);
	sort(ord.begin(), ord.end());
	
	map<int, int8_t> mp;
	for(int i=0; i<ord.size(); ++i) {
		mp[ord[i]] = i;
	}
	
	for(int i=0; i<vec.size(); ++i)
	{
		shr.push_back(mp[vec[i]]);
	}
}

bool check(const vector<int8_t> &vec)
{
	bool inc = true;
	for(int i=1; i<vec.size(); ++i)
	{
		if (inc)
		{
			if (vec[i-1] > vec[i]) inc = false;
		}
		else 
		{
			if (vec[i-1] < vec[i]) 
				return false;
		}
	}
	
	return true;
}

int main()
{
	int T_inp; cin >> T_inp;
	for(int T=1; T<=T_inp; ++T)
	{
		int N; cin >> N;
		
		vector<int> vec(N);
		for(int i=0; i<vec.size(); ++i) cin >> vec[i];
		
		vector<int8_t> shr;
		make_short(shr, vec);
		
		// ALGO
		map<vector<int8_t>, bool> used;
		if (check(shr))
		{
			printf("Case #%d: %d\n", T, 0);
			continue;
		}
		used[shr] = true;
		
		// Not found
		queue<vector<int8_t> > one, two;
		one.push(shr);
		
		bool found = false;
		for(int i=1; !found ;++i)
		{
			queue<vector<int8_t> > &que = (i&1 ? one:two);
			queue<vector<int8_t> > &next = (i&1 ? two:one);
			
			while(!que.empty() && !found)
			{
				vector<int8_t> cur = que.front();
				que.pop();
				
				for(int p=1; p<cur.size(); ++p)
				{
					vector<int8_t> cp(cur);
					swap(cp[p-1], cp[p]);
					
					if (!used[cp])
					{
						//cout << "\nSTEP - ";
						//for(int j=0; j<cp.size(); ++j) cout << (int)cp[j] << " ";
						
						if (check(cp))
						{
							found = true;
							break;
						}
						
						next.push(cp);
						used[cp] = true;
					}
				}
			}
			
			if (found)
			{
				printf("Case #%d: %d\n", T, i);
				break;
			}
		}
	}
	return 0;
}