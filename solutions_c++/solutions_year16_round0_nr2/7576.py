#include <iostream>
#include <queue>
#include <map>

using namespace std;

int main() {
	int cases;
	cin >> cases;

	int counter=1;
	while(cases--) {
		string s;
		cin >> s;
		

		map<string, int> seen;
		queue<string> q;

		seen[s] = 0;
		q.push(s);
	
		while(!q.empty()) {
			string top = q.front();
			q.pop();

			bool b=true;
			for(char ch : top)
				if(ch == '-')
					b=false;

			if(b) {
				cout << "Case #" << counter++ << ": " << seen[top] << endl;
			}

			for(int i=0; i<top.length(); i++) {
				string next = top;

				for(int j=0; j<=i; j++) {
					if(next[j] == '-')
						next[j] = '+';
					else
						next[j] = '-';
				}

				if(seen.count(next)==0) {
					q.push(next);
					seen[next] = seen[top]+1;
				}
			}

		}
	

	}


	return 0;
}