#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define SZ(v) ((int)((v).size()))
#define LE(s) ((int)((s).length()))
#define ALL(v) v.begin(), v.end()

struct tree_t{
	tree_t(char car, string str){
		curr = car;
		list = str;
	}
	char curr;
	string list;
	bool operator < (const tree_t & other) const {
		return (list < other.list);
	}
};

bool wins(tree_t &a, tree_t &b){
	return ((a.curr == 'R' && b.curr == 'S') || (a.curr == 'S' && b.curr == 'P') || (a.curr == 'P' && b.curr == 'R'));
}

bool sort_vec(vector<tree_t> &a, vector<tree_t> &b){
	return (a.size() >= b.size());
}
		

vector<vector<tree_t> > sort_trees(vector<tree_t> &vec){
	vector<vector<tree_t> > sol = vector<vector<tree_t> >(3, vector<tree_t>());
	for (tree_t &t : vec) {
		if (t.curr == 'R')
			sol[0].pb(t);
		else if (t.curr == 'P')
			sol[1].pb(t);
		else if (t.curr == 'S')
			sol[2].pb(t);
		else
			cout << "ERROR";
	}
	sort(ALL(sol[0]));
	sort(ALL(sol[1]));
	sort(ALL(sol[2]));
	sort(ALL(sol), sort_vec);
	return sol;
}

tree_t eval(vector<tree_t> vec) {
	if (vec.size() == 1) {
		return vec[0];
	}
	vector<vector<tree_t> > sorted = sort_trees(vec);
	if (sorted[0].size() > vec.size()/2){
		return tree_t('o', "");
	}
	vector<tree_t> new_;
	unsigned int ind_0 = 0, ind_1 = 0, ind_2 = 0;
	while (ind_0 != sorted[0].size() || ind_1 != sorted[1].size() || ind_2 != sorted[2].size()) {
		unsigned int left_0 = sorted[0].size() - ind_0;
		unsigned int left_1 = sorted[1].size() - ind_1;
		unsigned int left_2 = sorted[2].size() - ind_2;
		for (unsigned int i=0; i<left_0 - left_2;i++){
			char win;
			if (wins(sorted[0][0], sorted[1][0]))
				win = sorted[0][0].curr;
			else
				win = sorted[1][0].curr;
			if (sorted[0][ind_0].list < sorted[1][ind_1].list)
				new_.pb(tree_t(win, sorted[0][ind_0].list + sorted[1][ind_1].list));
			else
				new_.pb(tree_t(win, sorted[1][ind_1].list + sorted[0][ind_0].list));
			ind_0++;
			ind_1++;
		}
		for (unsigned int i=0; i<left_0 - left_1; i++){
			char win;
			if (wins(sorted[0][0], sorted[2][0]))
				win = sorted[0][0].curr;
			else
				win = sorted[2][0].curr;
			if (sorted[0][ind_0].list < sorted[2][ind_2].list)
				new_.pb(tree_t(win, sorted[0][ind_0].list + sorted[2][ind_2].list));
			else
				new_.pb(tree_t(win, sorted[2][ind_2].list + sorted[0][ind_0].list));
			ind_0++;
			ind_2++;
		}
		left_0 = sorted[0].size() - ind_0;
		left_1 = sorted[1].size() - ind_1;
		left_2 = sorted[2].size() - ind_2;
		if (left_0 == left_1 && left_2 > 0){
			char win;
			if (wins(sorted[2][0], sorted[0][0]))
				win = sorted[2][0].curr;
			else
				win = sorted[0][0].curr;
			if (sorted[0][ind_0].list < sorted[2][ind_2].list)
				new_.pb(tree_t(win, sorted[0][ind_0].list + sorted[2][ind_2].list));
			else
				new_.pb(tree_t(win, sorted[2][ind_2].list + sorted[0][ind_0].list));
			ind_0++;
			ind_2++;
			if (wins(sorted[1][0], sorted[2][0]))
				win = sorted[1][0].curr;
			else
				win = sorted[2][0].curr;
			if (sorted[1][ind_1].list < sorted[2][ind_2].list)
				new_.pb(tree_t(win, sorted[1][ind_1].list + sorted[2][ind_2].list));
			else
				new_.pb(tree_t(win, sorted[2][ind_2].list + sorted[1][ind_1].list));
			ind_1++;
			ind_2++;
		}
	}
	return eval(new_);
}
	


int main(){
	cin.sync_with_stdio(false);
	int T;
	cin >> T;
	for (int i=0; i<T; i++){
		int N, R, P, S;
		cin >> N >> R >> P >> S;
		vector<tree_t> vec;
		while (R--){
			vec.pb(tree_t('R', "R"));
		}
		while (P--){
			vec.pb(tree_t('P', "P"));
		}
		while (S--){
			vec.pb(tree_t('S', "S"));
		}
		tree_t sol = eval(vec);
		cout << "Case #" << i + 1 << ": ";
		if (sol.curr == 'o'){
			cout << "IMPOSSIBLE\n";
		}
		else{
			cout << sol.list << endl;
		}
	}
}
