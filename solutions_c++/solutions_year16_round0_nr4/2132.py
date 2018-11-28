# include <bits/stdc++.h>
using namespace std;

vector<string> sim;
vector<string> gol;

void add(string s, int l, int r)
{
	if (l == r) sim.push_back(s);
	else {
		add(s + 'G', l+1, r);
		add(s + 'L', l+1, r);
	}
}

void gen()
{
	int K = 3, C = 3;
	add("", 0, K);
	
	string g_dan;
	for(int i=0; i<K; ++i) g_dan += 'G';
	
	for(auto s:sim) {
		string new_s = s;
		for(int i=1; i<C; ++i) {
			string t;
			for(int p=0; p<new_s.size(); ++p) {
				t += (new_s[p] == 'G' ? g_dan:s);
			}
			new_s = t;
		}
		printf("%s: %s\n", s.c_str(), new_s.c_str());
	}
}

void d_simp()
{
	int T; cin >> T;
	for(int T_=1; T_<=T; ++T_) {
		int k, c, s; cin >> k >> c >> s;
	
		printf("Case #%d: ", T_);
		for(int i=1; i<=k; ++i) printf("%d ", i);
		printf("\n");
	}
}

int main()
{		
	d_simp();
	exit(0);
	
	gen();
	exit(0);
	
	int T; cin >> T;
	for(int T_=1; T_<=T; ++T_) {
		int k, c, s; cin >> k >> c >> s;
		
		printf("Case #%d: ", T_);
		
		int s_ = (k+c-1)/c;
		if (s < s_) printf("IMPOSSIBLE\n");
		else {
			if (c == 1) {
				for(int i=1; i<=k; ++i) {
					printf("%d ", i);
				}
				printf("\n");
			}
			else {
				printf("HOPE!\n");
			}
		}
	}
	return 0;
}