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
#include<deque>
#include<stack>
#include<ctime>
#include<bitset>
#include<set>
using namespace std;
typedef long long ll;
int n,r,p,s; 
map<pair<int,int>,string> m[13]; 
void init() {
	for(int i=0;i<3;++i) {
		queue<int> qu;
		qu.push(i);
		int dep = 0;
		
		for(;dep<=12;++dep) {
			int a[3]={
				0,0,0
			};
			string ans;
			for(int j=qu.size();j>0;--j) {
				++a[qu.front()];
				switch(qu.front()) {
					case 0:
						ans.push_back('R');
						qu.push(1); 
						qu.push(0); 
						break;
					case 1:
						ans.push_back('P');
						qu.push(1); 
						qu.push(2);
						break;
					case 2:
						ans.push_back('S');
						qu.push(0); 
						qu.push(2);
						break;
				}
				qu.pop();
			}
			map<pair<int,int>,string>::iterator x = m[dep].find(make_pair(a[0],a[1]));
			if(x==m[dep].end()||x->second < ans)
				m[dep][make_pair(a[0],a[1])] = ans;
		}
	}
}
void deal(string &s,int l,int r) {
	if(l+1==r)
		return;
	int mid = (l+r)/2;
	int len = (r-l+1)/2;
	deal(s,l,mid);
	deal(s,mid+1,r);
	if(s.substr(l,len)>s.substr(mid+1,len)) {
		for(int i=l;i<l+len;++i) {
			char x = s[i];
			s[i] = s[i+len];
			s[i+len] = x;
		}
	}
}
void gao(){
	scanf("%d%d%d%d",&n,&r,&p,&s);
	map<pair<int,int>,string>::iterator x = m[n].find(make_pair(r,p));
	if(x!=m[n].end()) {
		string xx = x->second;
		deal(xx,0,xx.length()-1);
		cout<<xx<<endl; 
	} else {
		cout<<"IMPOSSIBLE"<<endl;
	}
}
void usefile(string fn) {
	freopen((fn+".in").c_str(),"r",stdin);
	freopen((fn+".out").c_str(),"w",stdout);
} 
int main() {
	usefile("A-large"); 
	init();
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;++i) {
		printf("Case #%d: ", i);
		gao();
	}
	return 0;
}