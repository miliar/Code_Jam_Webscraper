/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <bitset>
#include <iomanip>
#include <utility>

using namespace std;

typedef long long LL;
typedef complex<double> point;
typedef long double ldb;
typedef pair<int,int> pii;

const int inf = 1000000000;

bool good[1<<22];
int N=0;
int dp[4010][12][12][12];
int Q[1000][1000],len[1000];
string s;

struct node{
	int child[26];
	node() { memset(child, -1, sizeof child); }
}tree[1<<22];

inline void makeTrie(){
	ifstream inp("garbled_email_dictionary.txt");
//	ifstream inp("dict.txt");
	string s;
	N=1;
	good[0] = true;
	while (inp >> s){
		int cur = 0;
		for (int i=0; i<(int)s.size(); i++){
			if (tree[cur].child[s[i]-'a']==-1)
				tree[cur].child[s[i]-'a']= N++;
			cur = tree[cur].child[s[i]-'a'];
		}
		good[cur] = true;
//		cerr << "CUR " << cur << endl;
	}
	inp.close();
}

inline vector<bool> check(int pos, int f1, int f2){
	vector <bool> mark(14, false);
//	cerr << pos << ' ' << f1 << ' ' << f2 << ' ' << "THIS" << endl;
	mark[0] = 1;
	Q[0][0] = 0; len[0] = 1;
	for (int rep=0; len[rep]; rep++){
		len[rep+1] = 0;
		if (pos == (int)s.size())
			break;
		for (int i=0; i<len[rep]; i++){
			int cur = Q[rep][i];
	//		cerr << "rep " << cur << endl;
			if (pos!=f1 && pos!=f2){
				if (tree[cur].child[s[pos]-'a']!=-1){
					Q[rep+1][len[rep+1]++] = tree[cur].child[s[pos]-'a'];
					mark[rep+1]= (mark[rep+1] || (good[tree[cur].child[s[pos]-'a']]));
				}
			}else{
				for (int j=0; j<26; j++) if (tree[cur].child[j]!=-1){
					Q[rep+1][len[rep+1]++] = tree[cur].child[j];
					mark[rep+1] = (mark[rep+1] || good[tree[cur].child[j]]); 
				}
			}
		}
		pos++;
	}
	return mark;
}

inline int go (int pos, int sat, int f1, int f2){
	f1 = min(f1, 11);
	f2 = min(f2, 11);
	if (f1<f2) swap(f1,f2);
	int &ret = dp[pos][sat][f1][f2];
	if (ret != -1)
		return ret;
	vector <bool> mark = check(pos-sat, pos-f1, pos-f2);
	if (pos == (int)s.size()){
//		cerr << ":) " << sat << ' ' << f1 << ' ' << f2 << endl;
		return ret = (mark[sat]) ? (0) : (inf);
	}
	ret = inf;
	for (int i=1; i<=sat; i++) if (mark[i]){
	//	cerr << pos << ' ' << f1 << ' ' << f2 << endl;
		ret = min(ret, go(pos, sat-i, f1, f2));
	}
	if (sat<=9){
		ret = min(ret, go(pos+1, sat+1, f1+1, f2+1));
		if (f2>=5)
			ret = min(ret, go(pos+1, sat+1, f2+1, 1) + 1);
	}
	return ret;
}

inline void main2(){
	cin >> s;
//	vector <bool> mark = check(0, -1, -1);
//	for (int i=0; i<(int)mark.size(); i++){
//		cerr << i << " : " << mark[i] << endl;
//	}
	memset(dp, -1, sizeof dp);
	cout << go(0, 0, 11, 11) << endl;
//	cout << s << " : " << go(0, 0, 11, 11) << endl;
}

int main(){
	makeTrie();
	int testCase; cin >> testCase;
	for (int o=1; o<=testCase; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
