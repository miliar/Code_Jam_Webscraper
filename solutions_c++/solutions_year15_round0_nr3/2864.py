// dijkstra #codejam2015
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>

#define pb push_back
#define po pop_back

using namespace std;

int l, m;
string c;
string in;

int sign = 1;
vector<int> fori;
vector<int> signi;
int fork[10005];
int signk[10005];

char func (char x, char y) {
	if (x == '1') {
		if (y == '1') {
			return '1';
		} else if (y == 'i') {
			return 'i';
		} else if (y == 'j') {
			return 'j';
		} else if (y == 'k') {
			return 'k';
		}
	} else if (x == 'i') {
		if (y == '1') {
			return 'i';
		} else if (y == 'i') {
			sign *= -1;
			return '1';
		} else if (y == 'j') {
			return 'k';
		} else if (y == 'k') {
			sign *= -1;
			return 'j';
		}
	} else if (x == 'j') {
		if (y == '1') {
			return 'j';
		} else if (y == 'i') {
			sign *= -1;
			return 'k';
		} else if (y == 'j') {
			sign *= -1;
			return '1';
		} else if (y == 'k') {
			return 'i';
		}
	} else if (x == 'k') {
		if (y == '1') {
			return 'k';
		} else if (y == 'i') {
			return 'j';
		} else if (y == 'j') {
			sign *= -1;
			return 'i';
		} else if (y == 'k') {
			sign *= -1;
			return '1';
		}
	}

	return '?';
}

void buildFori() {
	sign = 1;
	char last = in[0];
	if (last == 'i') {
		fori.pb(1);
		signi.pb(sign);
	}
	for (int i=1;i<in.size();i++) {
		last = func(last, in[i]);
		if (last == 'i') {
			fori.pb(i+1);
			signi.pb(sign);
		}
	}
}

void buildFork() {
	sign = 1;
	char last = in[in.size()-1];
	if (last == 'k')  {
		fork[in.size()-1] = 1;
		signk[in.size()-1] = sign;
	}
	for (int i=in.size()-2;i>=0;i--) {
		last = func(in[i], last);
		if (last == 'k') {
			fork[i] = 1;
			signk[i] = sign;
		}
	}
}

bool check() {
	for (int i=0;i<fori.size();i++) {
		int startP = fori[i];
		char last = in[startP];
		sign = 1;
		int signa = signi[i];
		if (last == 'j') {
			if (fork[startP+1] && signa * sign * signk[startP+1] == 1) {
				cout<<"YES";
				return true;
			}
		}
		for (int j=startP + 1; j < in.size(); j++) {
			last = func(last, in[j]);
			if (last == 'j') {
				if (fork[j+1] && signa * sign * signk[j+1] == 1) {
					cout<<"YES";
					return true;
				}
			}
		}
	}

	return false;
}

void solve() {
	sign = 1;
	fori.resize(0);
	signi.resize(0);
	memset(fork, 0, sizeof(fork));
	memset(signk, 0, sizeof(signk));

	cin>>l>>m;
	cin>>c;
	in = "";
	for (int i=1;i<=m;i++)
		in += c;

	buildFori();
	buildFork();
	
	if (!check())
		cout<<"NO";
}

int main() {

	int t;
	cin>>t;
	for (int i=1;i<=t;i++) {
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<'\n';
	}

	return 0;
}