#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 
#include <fstream>
using namespace std;
const double eps=1e-8;
const int maxn=100005;
typedef long long ll;
typedef pair<int,int> pii;
int t;
int l;
int x;

int foo(char& c,char haha) {
	if(c=='1') {
		if(haha=='1') {c='1';return 0;}
		if(haha=='i') {c='i';return 0;}
		if(haha=='j') {c='j';return 0;}
		if(haha=='k') {c='k';return 0;}
	}
	if(c=='i') {
		if(haha==1) {c='i';return 0;}
		if(haha=='i') {c='1';return 1;}
		if(haha=='j') {c='k';return 0;}
		if(haha=='k') {c='j';return 1;}
	}
	if(c=='j') {
		if(haha==1) {c='j';return 0;}
		if(haha=='i') {c='k';return 1;}
		if(haha=='j') {c='1';return 1;}
		if(haha=='k') {c='i';return 0;}
	}
	if(c=='k') {
		if(haha==1) {c='k';return 0;}
		if(haha=='i') {c='j';return 0;}
		if(haha=='j') {c='i';return 1;}
		if(haha=='k') {c='1';return 1;}
	}
}
string s;
string str;
int main() {
	ifstream cin("C-small-attempt1.in");
	ofstream cout("C-small-attempt1.out");
	int kase=1;
	cin>>t;
	while(t--) {
		cin>>l>>x;
		//printf("%d %d\n",l,x);
		s.clear();
		str.clear();
		for(int i=0;i<l;i++) {
			char c;
			cin>>c;
			//printf("%c",c);
			s+=c;
		}
		for(int i=0;i<x;i++) str+=s;
		char c;
		int cnt=0;
		bool f1=0,f2=0,f3=0;
		for(int i=0;i<str.size();i++) {
			if(!i) c=str[i];
			else cnt+=foo(c,str[i]);
			if(!f1&&c=='i'&&cnt%2==0) f1=1;
			if(f1&&c=='k'&&cnt%2==0) f2=1;
		}
		if(f2&&c=='1'&&cnt%2) f3=1;
		cout<<"Case #"<<kase++<<": ";
		if(f1&&f2&&f3) cout<<"YES\n";
		else cout<<"NO\n";
	}


	return 0;
}
