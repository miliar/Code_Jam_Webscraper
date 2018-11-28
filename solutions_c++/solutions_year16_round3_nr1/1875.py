#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <functional>

using namespace std;

void execute()
{
	priority_queue<pair<int, char>> pq;

	int n;
	cin >> n;

	for(int i=0; i<n; i++)
	{
		int cnt;
		cin >> cnt;
		pq.push(make_pair(cnt, i+'A'));
	}

	while (!pq.empty())
	{
		pair<int, char> tmp = pq.top();
		pq.pop();
		cout << tmp.second;
		if(--tmp.first) pq.push(tmp);

		if (pq.size() == 2 && pq.top().first == 1) {
			cout << " ";
			continue;
		}
		else if (pq.size() == 1) {
			cout << pq.top().second << endl;
			return;
		}

		tmp = pq.top();
		pq.pop();
		cout << tmp.second << " ";
		if(--tmp.first) pq.push(tmp);
	}
}


int main()
{
	int loop;
	cin >> loop;

	for (int i = 1; i <= loop; i++)
	{
		cout << "Case #" << i << ": ";
		execute();
	}
}