#include <iostream>
#include <vector>
#include <cstdio>
#include <sstream>
#include <map>
#include <string>
#include <algorithm>
#include <queue>
#include <cmath>
#include <set>
using namespace std;

map<char, map<char, pair<int,char> > > q;

void constract(){
	q['1']['1'] = {1,'1'};	q['1']['i'] = {1,'i'};	q['1']['j'] = {1,'j'};	q['1']['k'] = {1,'k'};
	q['i']['1'] = {1,'i'};	q['i']['i'] = {-1,'1'};	q['i']['j'] = {1,'k'};	q['i']['k'] = {-1,'j'};
	q['j']['1'] = {1,'j'};	q['j']['i'] = {-1,'k'};	q['j']['j'] = {-1,'1'};	q['j']['k'] = {1,'i'};
	q['k']['1'] = {1,'k'};	q['k']['i'] = {1,'j'};	q['k']['j'] = {-1,'i'};	q['k']['k'] = {-1,'1'};
}

struct quat{
	pair<int, char> val;
	quat operator*(const quat& x){
		quat ret;
		ret.val = q[this->val.second][x.val.second];
		ret.val.first *= this->val.first * x.val.first;
		return ret;
	}
};

//segment tree
//using std::function as comparing function
template<class Value = int>
class SegmentTree{
	int n;
	vector<Value> V;
	Value DEFAULT_VALUE;

	//evaluation function
	static Value default_evaluate(Value a, Value b){
		return a*b;
	}

	function< Value(Value, Value) > evaluate;

	//return evaluated value in [a,b)
	//T[at] covers [l,r)
	Value RangeEvaluation(int a, int b, int at, int l, int r){
		//out of range
		if(r <= a || b <= l) return DEFAULT_VALUE;
		//covered
		if(a <= l && r <= b) return V[at];

		//partially covered
		else{
			Value val_left = RangeEvaluation(a,b, at*2+1, l, (l+r)/2);
			Value val_right = RangeEvaluation(a,b, at*2+2, (l+r)/2, r);
			return evaluate(val_left, val_right);
		}
	}

public:
	SegmentTree(int size, Value DEFAULT = 0, function< Value(Value, Value) > eval = default_evaluate){
		DEFAULT_VALUE = DEFAULT;
		evaluate = eval;
		n=1;
		while(n<size) n <<= 1;
		V = vector<Value>(2*n - 1, DEFAULT_VALUE);
	}

	void update(int at, Value new_val){
		at += n-1;
		V[at] = new_val;
		while(at>0){
			at = (at-1)/2;
			V[at] = evaluate(V[at*2 + 1], V[at*2 + 2]);
		}
	}


	//return evaluated value in [l,r)
	Value RangeEvaluation(int l, int r){
		if(l>=r) return DEFAULT_VALUE;
		if(l>=n) return DEFAULT_VALUE;
		return RangeEvaluation(l,r, 0, 0, n);
	}
};


string solve(){
	long long L,X;
	cin >> L >> X;
	string S;
	cin >> S;
	string my_s;

	set<char> z;
	for(int i=0; i<L; i++){
		z.insert(S[i]);
	}
	if(z.size() <= 1 || L*X<=2){
		return "NO";
	}

	for(int k=0; k<X; k++){
		my_s += S;
	}
	SegmentTree<quat> seg(my_s.size(), {{1,'1'}});
	for(int i=0; i<my_s.size(); i++){
		seg.update(i, {{1,my_s[i]}});
	}

	//[0,j) => i
	quat my_i = {{1,my_s[0]}};
	for(int j=1; j<my_s.size(); j++){
		if(j>1) my_i = my_i * (quat){{1,my_s[j-1]}};
		if(my_i.val.first != 1 || my_i.val.second != 'i') continue;

		quat my_j = {{1,my_s[j]}};
		//[j,k) => j
		for(int k=j+1; k<my_s.size(); k++){
			if(k>j+1) my_j = my_j * (quat){{1,my_s[k-1]}};
			if(my_j.val.first != 1 || my_j.val.second != 'j') continue;

			//[k,my_s.size()) => k
			quat my_k = seg.RangeEvaluation(k,my_s.size());
			if(my_k.val.first != 1 || my_k.val.second != 'k') continue;

			return "YES";
		}
	}
	return "NO";

}

int main(){
	constract();

	int T;
	cin >> T;
	for(int t=1; t<=T; t++){
		cerr << "case : " << t << endl;
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}