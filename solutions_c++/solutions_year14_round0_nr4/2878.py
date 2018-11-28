#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <utility>

using namespace std;

vector<double> naomi;
vector<double> ken;

string int_to_string ( int n )
{
	stringstream ss;
	ss << n;
	return ss.str();
}

pair<string, string> solve(int N) {
	int pts = 0, dpts = 0;
	
	sort(naomi.begin(), naomi.end());
	sort(ken.begin(), ken.end());
	//Solution start
	int k_most, n_least, k_least, n_most;
	//deceitful war
	k_most = ken.size() - 1;
	k_least = 0;
	n_least = 0;
	for(int rep = 0; rep < N; rep++) {
		if(naomi[n_least] > ken[k_least]) {
			dpts++;
			k_least++;
		} else {
			k_most--;
		}
		n_least++;
	}
	//war
	n_most = naomi.size() - 1;
	k_least = 0;
	k_most = ken.size() - 1;
	for(int rep = 0; rep < N; rep++) {
		if(naomi[n_most] > ken[k_most])
		{ pts++; n_most--; k_least++; }
		else
		{ k_most--; n_most--; }
	}
	//Solution end

	return make_pair(int_to_string(dpts), int_to_string(pts));
}

int main(void) 
{
	int TC;
	cin >> TC;
	for(int tc = 0; tc < TC; tc++) {
		int N;
		cin >> N;
		naomi.resize(N);
		ken.resize(N);
		for(int i = 0; i < N; i++) cin >> naomi[i];
		for(int i = 0; i < N; i++) cin >> ken[i];
		pair<string, string> p = solve(N);
		cout << "Case #" << (tc + 1) << ": " << p.first << " " << p.second << endl;
	}
	return 0;
}
