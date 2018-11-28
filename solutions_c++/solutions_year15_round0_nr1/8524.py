#include <iostream>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <cctype>
#include <tuple>

using namespace std;

int invite(int n, string a) {
	int count = a[0] - '0', friends = 0;
	for(int i = 1; i <= n; i++) {
		int audiance = a[i] - '0';
		int offset = (count >= i)? 0 : (i - count);
		friends += offset;
		count += offset + audiance;
	}
	return friends;
}

int main() {
int n, s_max, i = 1;

string a;
cin>>n;

for(int i = 1; i <= n; i++) {
	cin>>s_max>>a;
	cout<<"Case #"<<i<<": "<<invite(s_max, a)<<endl;
}
