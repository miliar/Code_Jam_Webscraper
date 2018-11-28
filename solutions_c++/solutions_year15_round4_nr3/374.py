#include<bits/stdc++.h>
using namespace std;

vector<int> s[25];
vector<int> v[25];
string h;
int countt;
map<string, int> M;
int m[100005];


bool valid(char c) {
	if (c >= 'a' && c <= 'z')
		return true;
	return false;
}

void addEnglish(int &s) {
	if (m[s] == 0)
		m[s] = 1;
	else if (m[s] == 2) {
		m[s] = 3, countt++;
	}
}

void addFrench(int &s) {
	if (m[s] == 0)
		m[s] = 2;
	else if (m[s] == 1) {
		m[s] = 3, countt++;
	}
}


bool isEnglish(int &s) {
	if (m[s] != 2 && m[s] != 0)
		return true;
	return false;
}


bool isFrench(int &s) {
	if (m[s] != 1 && m[s] != 0)
		return true;
	return false;
}

void removeEnglish(int &s) {
	if (m[s] == 1)
		m[s] = 0;
	else if (m[s] == 3)
		m[s] = 2, countt--;
}

void removeFrench(int &s) {
	if (m[s] == 2)
		m[s] = 0;
	else if (m[s] == 3)
		m[s] = 1, countt--;
}



int main() {
	freopen("/home/ahmed_ossama/Round 2/Task C/C-small-attempt1.in", "r", stdin);
	freopen("/home/ahmed_ossama/Round 2/Task C/C-small-attempt1.out", "w", stdout);

	int t;
	int id = 1;
	cin >> t;
	while (t--) {
		cerr << t << endl;
		int n;
		cin >> n;
		M.clear();
		int index = 0;
		getline(cin, h);
		for (int i = 0; i < n; i++) {
			getline(cin, h);
			s[i].clear();
			int ind = 0;
			while (ind < int(h.size())) {
				while (ind < int(h.size()) && !valid(h[ind]))
					ind++;
				string word = "";
				while (ind < int(h.size()) && valid(h[ind]))
					word += h[ind++];
				while (ind < int(h.size()) && !valid(h[ind]))
					ind++;
				if (word.size()) {
					if (M.find(word) == M.end())
						M[word] = index++;
					s[i].push_back(M[word]);
				}
			}
		}
		countt = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < int(s[i].size()); j++)
				m[s[i][j]] = 0;


		for (int i = 0; i < int(s[0].size()); i++)
			addEnglish(s[0][i]);
		for (int i = 0; i < int(s[1].size()); i++)
			addFrench(s[1][i]);

		int ans = 1e9;
		for (int msk = 0; msk < (1 << (n - 2)); msk++) {

			for (int i = 2; i < n; i++)
				v[i].clear();
			for (int i = 2; i < n; i++) {
				if (msk & (1 << (i - 2))) {
					// french
					for (int j = 0; j < int(s[i].size()); j++)
						if (!isFrench(s[i][j])) {
							v[i].push_back(j);
							addFrench(s[i][j]);
						}
				}
				else {
					// english
					for (int j = 0; j < int(s[i].size()); j++)
						if (!isEnglish(s[i][j])) {
							v[i].push_back(j);
							addEnglish(s[i][j]);
						}
				}
			}
			ans = min(ans, countt);
			for (int i = 2; i < n; i++) {
				if (msk & (1 << (i - 2))) {
					// french
					for (int j = 0; j < int(v[i].size()); j++)
						removeFrench(s[i][v[i][j]]);
				}
				else {
					// english
					for (int j = 0; j < int(v[i].size()); j++)
						removeEnglish(s[i][v[i][j]]);
				}
			}
		}
		cout << "Case #" << id++ << ": " << ans << endl;

	}


}

