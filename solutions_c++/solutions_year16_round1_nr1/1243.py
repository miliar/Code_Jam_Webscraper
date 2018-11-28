#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<map>
#include<algorithm>
#include<vector>
#include<queue>
#include<cmath>
#include <deque>
#include<ctime>
using namespace std;
typedef long long ll;
void useFile(const string &name) {
	freopen((name + ".in").c_str(), "r", stdin);
	freopen((name + ".out").c_str(), "w", stdout);
}
void deal() {
	string s;
	cin>>s;
	deque<char> q;
	q.push_back(s[0]);
	for(int i=1;i<s.length();++i) {
		if(s[i]>=q.front())
			q.push_front(s[i]);
		else
			q.push_back(s[i]);
	}
	while(!q.empty()) {
		cout<<q.front();
		q.pop_front();
	}
	cout<<endl;
}
int main() {
	int n;
	useFile("A-large");
	cin>>n;
	for(int i=1;i<=n;++i){
		cout<<"Case #"<<i<<": ";
		deal();
	}
	return 0;
}
