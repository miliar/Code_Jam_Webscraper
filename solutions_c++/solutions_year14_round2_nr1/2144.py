#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <utility>
using namespace std;


int n,ans;
string str[100];
vector<char> v;
bool ans_ex;

void check() {
	for(int i=1;i<n;++i) {
		if(ans_ex) {
			string s=str[i];
			char prev=s[0];
			if(v[0]!=prev) ans_ex=0;
			int ctr=1;
			for(int j=1;j<s.length();++j) {
				if(s[j]!=prev) {
					if(ctr==v.size()) {
						ans_ex=0;
						break;
					}
					if(v[ctr++]!=s[j]) {
						ans_ex=0;
						break;
					}
					prev=s[j];
				}
			}
			if(ans_ex) {
				if(ctr==v.size()-1) ans_ex=0;
			}
		}
	}
}

void process() {
	v.clear();
	string s=str[0];
	char prev=s[0];
	v.push_back(prev);
	for(int i=1;i<s.length();++i) {
		if(s[i]!=prev) {
			v.push_back(s[i]);
			prev=s[i];
		}
	}
}
vector<int> lv;
map<pair<int,int>,int> m;

int myabs(int x) {
	if(x<0) return -1*x;
	else return x;
}
int find_all(int alp) {
	lv.clear();
	for(int i=0;i<n;++i) {
		lv.push_back(m[make_pair(i,alp)]);
	}
	int avg=0;
	for(int i=0;i<n;++i) {
		avg+=lv[i];
	}
	avg/=n;
	int lb,ub,rvl;
	sort(lv.begin(),lv.end());
	lb=lower_bound(lv.begin(),lv.end(),avg)-lv.begin();
	ub=upper_bound(lv.begin(),lv.end(),avg)-lv.begin();
	int lbans,ubans;
	lbans=ubans=0;
	for(int i=0;i<n;++i) {
		lbans+=myabs(lv[lb]-lv[i]);
		ubans+=myabs(lv[ub]-lv[i]);
	}
	rvl=min(lbans,ubans);
	return rvl;
}


void find_ans() {
	for(int i=0;i<n;++i) {
		int ctr=1;
		string s=str[i];
		char prev=s[0];
		int vid=0;
		for(int j=1;j<s.length();++j) {
			if(s[j]!=prev) {
				m[make_pair(i,vid)]=ctr;
				//cout<<i<<" "<<vid<<" "<<ctr<<"\n";
				prev=s[j];
				ctr=1;
				++vid;
			} else ++ctr;
		}
		m[make_pair(i,vid)]=ctr;
	}
	ans=0;
	for(int i=0;i<v.size();++i) {
		ans+=find_all(i);
	}
}

int main() {
	int tst;
	cin >> tst;
	for(int t=1;t<=tst;++t) {
		cout << "Case #" << t << ": ";
		cin >> n;
		ans_ex=1;
		for(int i=0;i<n;++i) {
			cin >> str[i];
		}
		process();
		check();
		if(!ans_ex) {
			cout << "Fegla Won";
		} else {
			find_ans();
			cout << ans;
		}
		cout << "\n";
	}
	return 0;
}
