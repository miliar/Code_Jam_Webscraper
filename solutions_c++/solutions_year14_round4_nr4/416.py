#include <iostream>
#include <string>
using namespace std;

string S[10];

struct node {
	int ptr[26];
	node() {
		for (int i = 0; i < 26; i++) {
			ptr[i] = -1;
		}
	}
};

node n[100000];
int num = 0;

int new_node() {
	n[num] = node();
	return num++;
}

int trie[4];

void insert(int i, int index, const string& s) {
	if (index == s.size()) return;
	if (n[i].ptr[s[index] - 'A'] == -1) {
		n[i].ptr[s[index] - 'A'] = new_node();
	}
	insert(n[i].ptr[s[index] - 'A'], index + 1, s);
}

int main() {
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++) {
		int M, N;
		cin >> M >> N;
		for (int i = 0; i < M; i++) {
			cin >> S[i];
		}
		int top = 1;
		for (int i = 0; i < M; i++) top *= N;
		int ans = -1;
		int counts = 0;
		for (int i = 0; i < top; i++) {
			num = 0;
			for (int j = 0; j < N; j++) {
				trie[j] = -1;
			}
			int temp = i;
			for (int j = 0; j < M; j++) {
				int select = temp % N;
				temp /= N;
				if (trie[select] == -1) {
					trie[select] = new_node();
				}
				insert(trie[select], 0, S[j]);
			}
			if (ans < num) {
				ans = num;
				counts = 1;
			}
			else if (ans == num) {
				counts++;
			}
		}
		cout << "Case #" << c << ": " << ans << " " << counts << endl;
	}
}