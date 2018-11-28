#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
using namespace std;

string solve(vector <int> item,int X) {
	int ans=0,i=0,j=item.size()-1;
	sort(item.begin(),item.end());
	while (i<j) {
		if (item[i] + item[j] <=X) {
			i++;
			j--;
		}
		else
			j--;
		ans++;
	}
	ans += i==j;
	return to_string(ans);
}

int main() {
	//freopen("A-small-attempt1.in", "rt", stdin); freopen("A-small.out", "wt", stdout);
	freopen("A-large.in", "rt", stdin); freopen("A-large.out", "wt", stdout);
	//freopen("test.in","rt",stdin);

	int T,t,N,X;
	cin>>T;
	for (int i=0; i<T; i++) {
		cin>>N>>X;
		vector <int> v;
		for (int j=0; j<N; j++) {
			cin>>t;
			v.push_back(t);
		}
		cout << "Case #" << i+1 << ": " << solve(v,X) << endl;
	}
}
