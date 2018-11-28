#include <iostream>
#include <set>

#define F first
#define S second

using namespace std;

int main() {

	int t, n, p, c = 0;
	set<pair<int,char> > st;
	set<pair<int,char> >::iterator it1, it2;
	cin >> t;
	for(int i = 1; i <= t; i++){
		st.clear(); c = 0;
		cout << "Case #"<< i << ": ";
		cin >> n;
		for(int j = 0; j < n; j++){
			cin >> p;
			c += p;
			st.insert(make_pair(p, (char)(j + 'A')));
		}
		while(c > 0) {
			it1 = st.end();
			it1--;
			it2 = it1;
			it2--;
			if((*it1).F == 1 && st.size() % 2 == 1){
				cout << (*it1).S << " ";
				c--;
				st.erase(it1);
			}
			else if((*it1).F - (*it2).F <= 1){
				cout << (*it1).S << (*it2).S << " ";
				int v1 = (*it1).F, v2 = (*it2).F;
				char c1 = (*it1).S, c2 = (*it2).S;
				st.erase(it1);
				st.erase(it2);
				v1--; v2--;
				if(v1){
					st.insert(make_pair(v1, c1));
				}
				if(v2){
					st.insert(make_pair(v2, c2));
				}
				c -= 2;
			}
			else {
				int v = (*it1).F;
				char c1 = (*it1).S;
				cout << c1 << c1 << " ";
				c -= 2;
				st.erase(it1);
				v -= 2;
				if(v){
					st.insert(make_pair(v, c1));
				}
			} 
		}
		cout << endl;
	}
	return 0;
}