#include <stdio.h>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int salary[1111111];
int parent[1111111];
vector<int> edges[1111111];

int minSalary[1111111];
int maxSalary[1111111];

pii people[1111111];

vector<int> trigger[1111111]; // trigger[needed maxSalary] = needed minSalary
int die[1111111];

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ", ++TK);

		int N = 0;
		int D = 0;
		scanf("%d %d",&N,&D);
		
		int As, Cs, Rs;
		scanf("%d %d %d %d",&salary[0],&As,&Cs,&Rs);
		for(int i = 1;i < N;i++) salary[i] = (salary[i-1] * (long long)As + Cs) % Rs;
		int Am, Cm, Rm;
		scanf("%d %d %d %d",&parent[0],&Am,&Cm,&Rm);
		for(int i = 1;i < N;i++) parent[i] = (parent[i-1] * (long long)Am + Cm) % Rm;

		parent[0] = -1;
		for(int i = 1;i < N;i++) parent[i] = parent[i] % i;
		for(int i = 0;i < N;i++) edges[i].clear();
		for(int i = 1;i < N;i++) edges[parent[i]].push_back(i);

		queue<int> q; q.push(0);
		minSalary[0] = maxSalary[0] = salary[0];
		while(!q.empty())
		{
			int x = q.front(); q.pop();

			for(auto y: edges[x])
			{
				minSalary[y] = min(minSalary[x], salary[y]);
				maxSalary[y] = max(maxSalary[x], salary[y]);
				q.push(y);
			}
		}

		for(int i = 0;i < N;i++) people[i] = pii(salary[i], i);
		sort(people, people+N);

		for(int i = 0;i < Rs;i++) trigger[i].clear();
		memset(die,0,sizeof(die[0]) * N);

		int ans = 0;
		int r = 0;
		int cnt = 0;
		for(int i = 0;i < N;i++)
		{
			while(r < N && people[r].first - people[i].first <= D)
			{
				if(trigger[people[r].first].size())
				{
					for(auto y: trigger[people[r].first])
					{
						if(y >= people[i].first)
						{
							die[y]++;
							cnt++;
						}
					}
					trigger[people[r].first].clear();
				}

				if(maxSalary[people[r].second] <= people[r].first && minSalary[people[r].second] >= people[i].first)
				{
					die[minSalary[people[r].second]]++;
					cnt++;
				}
				else if(minSalary[people[r].second] >= people[i].first)
				{
					trigger[maxSalary[people[r].second]].push_back(minSalary[people[r].second]);
				}
				r++;
			}
			ans = max(ans, cnt);

			if(people[i].second == 0) break;
			if(i+1 < N && people[i+1].first != people[i].first)
			{
				cnt -= die[people[i].first];
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
