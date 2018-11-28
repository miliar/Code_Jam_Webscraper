#include <iostream>
#include <fstream>
#include <string>
using namespace std;

static string ans = "";
static string tmp = "";

string find(string s) {
	if (s.length() == 1) {
		return s;
	}
	string s1 = find(s.substr(0, s.length()/2));
	string s2 = find(s.substr(s.length()/2, s.length()/2));
	if (s1.compare(s2) > 0) {
		return s2 + s1;
	} else return s1 + s2;
}

void dfs(int n, int r, int p, int s) {
	if (r < 0 || p < 0 || s < 0) return;
	if (n == 0) {
		string tmps = find(tmp);
		if (ans.empty() || ans.compare(tmps) > 0) {
			ans = tmps;
		}
		return;
	}
	int len = tmp.length();
	string tmp2 = tmp;
	tmp = "";
	int nr = 0, np = 0, ns = 0;
	for (int i = 0; i < len; ++i) {
		switch (tmp2[i]) {
			case 'P':
				tmp = tmp + "PR";
				++nr;
				break;
			case 'R':
				tmp = tmp + "RS";
				++ns;
				break;
			case 'S':
				tmp = tmp + "PS";
				++np;
				break;
		}
	}
	dfs(n-1, r - nr, p - np, s - ns);
	tmp = tmp2;
}

int main()
{
    //ifstream infile("A-small-attempt0.in");
    ifstream infile("A-large.in");
    ofstream outfile("A-output");
    int t;
    infile >> t;
    for (int ca = 1; ca <= t; ++ ca) {
    	outfile << "Case #" << ca << ": ";
    	ans = "";
    	int n, r, p, s;
    	infile >> n >> r >> p >> s;
    	tmp = "P";
    	dfs(n, r, p-1, s);                                                
    	tmp = "R";
    	dfs(n, r-1, p, s);
    	tmp = "S";
    	dfs(n, r, p, s-1);
    	if (ans == "") outfile << "IMPOSSIBLE" << endl;
    		else outfile << ans << endl;
    }

}