#include <iostream>
#include <queue>

using namespace std;

#define MAX_T 50
#define MAX_N 26

struct senator {
	char group;
	int count;
	bool operator<(const senator& rhs) const {
		return this->count < rhs.count;
	}
};

priority_queue<senator> Q;

int N;

void input()
{
	cin >> N;
	int count;
	for (int i = 0; i < N; i++) {
		cin >> count;
		Q.push({(char) ('A' + i), count });
	}
}

void test()
{
	for (int i = 1; i < 10; i++) {
		Q.push({ (char)('A' + i),i });
	}
	for (int i = 1; i < 10; i++) {
		cout << Q.top().group << Q.top().count << endl;
	}

	while (!Q.empty()) {
		cout << Q.top().group << Q.top().count << endl; 
		Q.pop();
	}
}

void process() {
	senator temp;
	while (!Q.empty()) {
		temp = Q.top(); 
		Q.pop();
		cout << temp.group;
		temp.count--;
		if(temp.count > 0) Q.push(temp);
		if (Q.empty()) break;
		temp = Q.top();
		Q.pop();
		temp.count--;
		if (temp.count > 0) {
			Q.push(temp);
			cout << temp.group;
		}
		else if(Q.size() == 1) {
			temp.count++;
			Q.push(temp);
		}
		else {
			cout << temp.group;
		}
		cout << " ";
	}
	cout << endl;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "CASE #" << i << ": ";
		input();
		process();
	}
	return 0;
}