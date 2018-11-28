#include <map>
#include <set>
#include <iostream>
#include <vector>
using namespace std;

int evacuate(vector<int>& v) {
	map<int, set<char>> m;
 	for(int i = 0; i < v.size(); ++i) {
		m[v[i]].insert(i+'A');
	}
	int cnt = 0;
	char c;
	while(m.size()>1 || (m.size() == 1 && m.find(1) == m.end())){
		cnt++; 
		if (m.rbegin()->second.size()){
			c = *(m.rbegin()->second.begin());
			m.rbegin()->second.erase(c);
			if (m.rbegin()->first > 1) {
				m[m.rbegin()->first-1].insert(c);
			}
		}
		if (m.rbegin()->second.size() == 0) {
			m.erase(std::prev(m.end()));
		}
		cout << c;
		if ((cnt == 2) || (m.size() == 1 && m.find(1) == m.end())) {
			cout << " ";
			cnt = 0;
		}
	}
	if (m.begin()->second.size()%2 == 1) {
		char ch = *(m.begin()->second.begin());
		m.begin()->second.erase(ch);
		cout << ch;
		cout << " ";
	} 
	int i = 0;
	for (auto e: m.begin()->second) {
		cout << e;
		if (i%2) cout << " ";
		i++;
	}
}
int main() {
	int T;
  	cin >> T;
  	int i = 0;
	while (i<T)	{
	    int N;
  		cin >> N;
  		vector<int> v(N);
  		int j = 0;
  		while(j<N) {
  			cin >> v[j];
  			j++;
  		}
  		cout << "Case #" << ++i << ": ";
  		evacuate(v);
  		cout <<endl; 
	}

}

	
	