//#pragma comment(linker, "/STACK:512000000")
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <stdlib.h>
#include <map>

using namespace std;

bool IsEq(string s1, string s2) {
	if (s1.size()!=s2.size()) return 0;
	for (int p=0;p<s1.size();++p)
		if (s1[p]!=s2[p]) return 0;
	return 1;
}

int main() {
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);

	int i,j,n,m,c,t,l;
	string st1,st2;
	vector<string> v,ans;
	vector<pair<char,int>> s1,s2;
	pair<char,int> ch;
	bool f;

	scanf("%d \n",&t);

	j=0;
	while (j<t) {
		scanf("%d \n",&n);
		f=0;
		l=0;
		//v.clear();
		//for (i=0;i<n;i++) {
		//	cin>>st;
		//	v.push_back(st);
		//}

		getline(cin,st1);
		getline(cin,st2);

		s1.clear();
		s2.clear();

		s1.push_back(make_pair(st1[0],1));
		c=0;
		for (i=1;i<st1.size();++i) {
			if (st1[i]==st1[i-1]) {
				s1[c].second++;
			}
			else {
				s1.push_back(make_pair(st1[i],1));
				c++;
			}
		}

		s2.push_back(make_pair(st2[0],1));
		c=0;
		for (i=1;i<st2.size();++i) {
			if (st2[i]==st2[i-1]) {
				s2[c].second++;
			}
			else {
				s2.push_back(make_pair(st2[i],1));
				c++;
			}
		}

		//ans.assign(n,"");
		//for (i=0;i<n;i++) {
		//	ans[i]+=v[i][0];
		//	c=0;
		//	for (m=1;m<v[i].size();++m) {
		//		if (v[i][m]!=ans[i][c]) {
		//			ans[i]+=v[i][m];
		//			c++;
		//		}
		//	}
		//}
		
		cout<<"Case #"<<j+1<<": ";

		if (s1.size()!=s2.size()) f=1;
		else
		{
			for (i=0;i<s1.size();++i) {
				if (s1[i].first!=s2[i].first) {
					f=1;
					break;
				}
				l+=abs(s1[i].second-s2[i].second);
			}
			if (!f) cout<<l<<endl;
		}

		if (f) cout<<"Fegla Won"<<endl;

		j++;
	}

    return 0;
}