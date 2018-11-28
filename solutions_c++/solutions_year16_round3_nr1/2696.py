#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pt;

struct CMP
{
	bool operator() (pt u, pt v){
		return u.second < v.second;
	}
};

priority_queue<pt, std::vector<pt>, CMP> q;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int test, n;
	scanf("%d\n", &test);
	int u;

	for (int t = 1; t <= test; t++){
		scanf("%d", &n);
		int sum = 0;

		for (int i = 0; i < n; i++){
			int u;

			scanf("%d", &u);
			q.push(make_pair(i, u));
			sum += u;
		}

		string res = "";
		pair<int, int> u;

		while (sum > 0){
			if ((q.size() == 2) &&  (sum- q.top().second == q.top().second)){
				int k = q.top().second;
				int x = q.top().first;
				q.pop();
				int y = q.top().first;
				q.pop();
				while (k --){
					res += (char) (x + 'A');
					res += (char) (y + 'A');
					if (k > 0)
						res += ' ';
				}
				break;
			} else {
				sum --;
				u = q.top();
				res += (char) (q.top().first + 'A');
				res += ' ';
				u.second --;
				q.pop();
				if (u.second > 0)
					q.push(u);
			}
		}

		printf("Case #%d: %s\n", t, res.c_str());
	}
}