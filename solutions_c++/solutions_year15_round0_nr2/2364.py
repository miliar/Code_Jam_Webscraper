#include <iostream>
#include <map>
#include <climits>

using namespace std;

void print(map <int, int, greater <int> > &m)
{
	cout << "--------MAP----------" << endl;
	for(auto i : m) {
		cout << "(" << i.first << " " << i.second << ") ";
	}
	cout << endl << "-------END-MAP----------" << endl;
}

int getAnswer(map <int, int, greater <int> > &m)
{
	int ans = m.begin()->first;
	int cur_step = 0;
	while(!m.empty() && (m.begin()->first > 2)) {
		++cur_step;
		int split_num = (m.begin()->first) / 2;
		int cur = m.begin()->first;
		int cur_num = m.begin()->second;
		if(m.size() > 1) {
			auto it = m.begin();
			++it;
			if(it->first * 2 < m.begin()->first) {
				split_num = it->first;
			}
		}
		m.erase(m.begin());
		m[split_num] += cur_num;
		m[cur - split_num] += cur_num;
		ans = min(ans, cur_step + m.begin()->first);
	}
	return ans;
}

int getAnswer2(map <int, int, greater <int> > m, int eat_num)
{
	int ans = m.begin()->first;
	int cur_step = 0;
	while(!m.empty() && (m.begin()->first > eat_num)) {
		int cur = m.begin()->first;
		int cur_num = m.begin()->second;
		cur_step += cur_num;
		m.erase(m.begin());
		m[eat_num] += cur_num;
		m[cur - eat_num] += cur_num;
		ans = min(ans, cur_step + m.begin()->first);
	}
	return ans;
}

int main()
{
	int tests_num, ans;
	cin >> tests_num;
	for(int t = 1; t <= tests_num; ++t) {
		map <int, int, greater <int> > m;
		int d, tmp;
		cin >> d;
		for(int i = 0; i < d; ++i) {
			cin >> tmp;
			if(m.find(tmp) == m.end()) {
				m[tmp] = 1;
			} else {
				++m[tmp];
			}
		}
		ans = m.begin()->first;
		for(int i = 2; i <= m.begin()->first; ++i) {
			ans = min(ans, getAnswer2(m, i));
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
