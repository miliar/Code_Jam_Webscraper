#include <iostream>
#include <string>
#include <queue>
#include <vector>

using namespace std;

int main() {
	int cases=0;
	cin >> cases;
	int caseNum=0;
	while (caseNum < cases) {
		caseNum++;
		cout << "Case #" << caseNum << ":";
		priority_queue<int, vector<int>, greater<int> > q;
		int n;
		cin >> n;
		for (int i=0; i<n*(2*n-1); i++){
			int x;
			cin >> x;
			q.push(x);
		}
		int current=0;
		int count=0;
		while (q.empty()==false) {
			if (q.top()==current)
				count++;

			else {
				if ((count%2)!=0) cout << " " << current;
				current=q.top();
				count=1;
			}
			q.pop();
		}
		if (count%2!=0) cout << " " << current;
		cout << endl;
	}
	return 0;
}

