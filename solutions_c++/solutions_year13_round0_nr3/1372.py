
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <deque>
#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

typedef long long LL;

bool check(LL a) {
	char ch[55];
	sprintf(ch, "%lld", a);
	int len = strlen(ch);
	for(int i=0, j=len-1;i<j;i++, j--) {
		if(ch[i] != ch[j]) return false;
	}
	return true;
}

vector<LL> v;

int main() {
	freopen("E:/TDDOWNLOAD/C-large-1.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	for(int i=1;i<=10000000;i++) {
		if(check(i) == false) continue;
		if(check(i*(LL)i)) v.push_back(i*(LL)i);
	}
	//cout<<v.size()<<endl;

	int T, Te=1;
	cin>>T;
	while(T--) {
		LL A, B;
		cin>>A>>B;
		int t1 = lower_bound(v.begin(), v.end(), A)-v.begin();
		int t2 = upper_bound(v.begin(), v.end(), B)-v.begin();
		printf("Case #%d: %d\n", Te++, t2-t1);
	}

}