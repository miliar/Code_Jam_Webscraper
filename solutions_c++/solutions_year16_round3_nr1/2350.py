#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <map>
#include <cstdio>
#include <fstream>
#include <string>
#include <set>
#include <stack>
#include <vector>
#include <queue>
using namespace std;

#define INF 2000000000
#define LLINF 20000000000000000LL

typedef long long ll;
typedef pair< int, int > pi;

int Q, N, M, K, L;
int A[30];
queue<int> q;
vector<int> r;

int main() {
	std::ifstream in("A-large.in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	std::ofstream out("out.txt");
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

	cin >> Q;
	for (int qq = 1; qq <= Q; qq++) {
		cin >> N;
		r.clear();
		for (int i = 0; i < N; i++) {
			cin >> A[i];
		}
		bool done = false;
		while (!done) {
			int maxv = 0;
			int maxes = 0;
			int count = 0;
			int C, D;
			while (!q.empty()) q.pop();
			for (int i = 0; i < N; i++) {
				if (A[i] > 0) count++;
				if (A[i] > maxv) {
					maxv = A[i];
					maxes = 1;
					C = i;
					while (!q.empty()) {
						int t = q.front(); q.pop();
						A[t] ++;
					}
					q.push(i);
					A[i] --;
				}
				else if (maxv != 0 && A[i] == maxv) {
					maxes++;
					D = i;
					q.push(i);
					A[i] --;
				}
			}
			if (count == 2 && maxes == 2) {
				cout << "Case #" << qq << ": ";
				for (int i = 0; i < r.size(); i++)
					cout << (char)(r[i] + 'A') << " ";
				while (maxv) {
					cout << (char)(C + 'A') << (char)(D + 'A') << " ";
					maxv--;
				}
				cout << "\n";
				done = true;
				break;
			}
			if (maxv == 0) break;
			while(!q.empty()) {
				r.push_back(q.front()); q.pop();
			}
		}
		if (!done) {
			cout << "Case #" << qq << ": ";
			for (int i = 0; i < r.size(); i++) {
				if (i == r.size() - 2) {
					cout << (char)(r[i] + 'A') << (char)(r[i + 1] + 'A') << "\n";
					break;
				}
				else
					cout << (char)(r[i] + 'A') << " ";
			}
		}
	}
}