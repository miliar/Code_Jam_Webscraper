#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <tuple>
#include <map>
#include <unordered_map>
#include <set>
#include <iostream>
#include <queue>
#include <array>

using namespace std;

struct Que
{
	array<int, 101> S;
	int dir;
	int depth;
	Que(const array<int, 101>& _s, int d, int depth)
	{
		S = _s;
		dir = d;
		this->depth = depth;
	}
	bool operator==(const Que& qq)
	{
		return S == qq.S && dir == qq.dir;
	}
};
int main()
{
	int tc;
	cin >> tc;
	for (int _ = 1; _ <= tc; _++)
	{
		string t;
		cin >> t;
		array<int, 101> ts;
		int l = t.size();
		for (int i = 0; i < l; i++)
		{
			ts[i] = t[i] == '-' ? 0 : 1;
		}


		queue<Que> Q;
		vector<Que> visit;
		visit.push_back(Que(ts, 1, 0));
		Q.push(Que(ts, 1, 0));
		while (!Q.empty())
		{
			auto q = Q.front();
			Q.pop();

			bool all1 = true;
			//printf("%d : ", q.depth);
			for (int i = 0; i<t.size(); i++)
			{
				if (q.S[i] == 0)
				{
					all1 = false;
					break;
				}
				//printf("%d", q.S[i]);
			}
			//printf("\n");
			if (all1)
			{
				printf("Case #%d: %d\n", _, q.depth);
				break;
			}

			if (q.dir == 1)
			{
				auto q2 = q; // q2 는 새로 들어갈 놈
				int differ = q2.S[0];
				for (int i = 0; i<t.size(); i++)
				{
					if (differ == q2.S[i])
						q2.S[i] = !q2.S[i];
					else
						break;
				}
				q2.depth++;
				if (find(visit.begin(), visit.end(), q2) == visit.end())
				{
					visit.push_back(q2);
					Q.push(q2);
				}

			}
			else
			{
				auto q2 = q; // q2 는 새로 들어갈 놈
				int differ = q2.S[t.size() - 1];
				for (int i = t.size() - 1; i >= 0; i--)
				{
					if (differ == q2.S[i])
						q2.S[i] = !q2.S[i];
					else
						break;
				}
				q2.depth++;
				if (find(visit.begin(), visit.end(), q2) == visit.end())
				{
					visit.push_back(q2);
					Q.push(q2);
				}
			}
			q.dir = !q.dir;
			q.depth++;
			if (find(visit.begin(), visit.end(), q) == visit.end())
			{
				visit.push_back(q);
				Q.push(q);
			}
			//Q.push(q); 
		}


	}





	return 0;
}
