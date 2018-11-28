#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;

int multi[4][4] = {{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};
map<pair<int,int>,bool> dicj,dick;
int sign(const int x){
	return x<0 ? -1 : 1;
}

//i:2   j:3   k:4
bool solve(vector<int>& s){
	for(int i=1;i<s.size();i++){
		int num = multi[abs(s[i-1])-1][abs(s[i])-1];
		int f = sign(s[i-1] * s[i]);
		s[i] = num * f;
	}
	for(int i=0;i<s.size();i++){
		for(int j=i+1;j<s.size();j++){
			if(s[i] == 2 && dicj[P(s[i],s[j])] && dick[P(s[j],s[s.size()-1])])return true;
		}
	}
	return false;
}

int main(void) {
	int t;
	cin >> t;
	dicj[P(1,3)] = true;
	dicj[P(2,4)] = true;
	dicj[P(3,-1)] = true;
	dicj[P(4,-2)] = true;
	dicj[P(-1,-3)] = true;
	dicj[P(-2,-4)] = true;
	dicj[P(-3,1)] = true;
	dicj[P(-4,2)] = true;
	dick[P(1,4)] = true;
	dick[P(2,-3)] = true;
	dick[P(3,2)] = true;
	dick[P(4,-1)] = true;
	dick[P(-1,-4)] = true;
	dick[P(-2,3)] = true;
	dick[P(-3,-2)] = true;
	dick[P(-4,1)] = true;
	for(int i=0;i<t;i++){
		int l,x;string t,s;
		cin >> l >> x >> t;
		for(int i=0;i<x;i++)s += t;
		vector<int> a(s.size());
		for(int i=0;i<s.size();i++){
			a[i] = s[i] - 'i' + 2;
		}
		cout << "Case #" << i+1 << ": " << (solve(a)?"YES":"NO") << endl;
	}
	
	return 0;
}

