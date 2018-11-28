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
int d;
int a[1005];
int calc(int lim,int x) {
	multiset<int> s;
	for(int i=0;i<d;i++) s.insert(a[i]);
	int cnt=0;
	while(x--) {
		int tmp=*s.rbegin();
		if(tmp>lim) {
			cnt++;
			s.erase(s.find(tmp));
			s.insert(lim);
			s.insert(tmp-lim);
		}
		else break;
	}
	return cnt+*s.rbegin();
}
bool check(int x) {
	for(int i=1;i<=x;i++) {
		if(calc(i,x-i)<=x) return 1;
	}
	return 0;
}
int main() {
	ifstream cin("B-small-attempt12.in");
	ofstream cout("B-small-attempt12.out");
	int kase=1;
	cin>>t;
	while(t--) {
		cin>>d;
		int tmp=-1;
		for(int i=0;i<d;i++) cin>>a[i],tmp=max(tmp,a[i]);
		int l=0,r=tmp;
		while(l<r) {
			int m=(l+r)/2;
			if(check(m)) r=m;
			else l=m+1;
		}
		cout<<"Case #"<<kase++<<": "<<r<<endl;
	}


	return 0;
}
