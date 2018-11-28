#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<stack>
#include<deque>
#include<queue>
#include<list>
using namespace std;
int maxgcd(int a, int b) {
	if(a<b) swap(a,b);
	while(a!=b) {
		a = a-b;
		if(a<b) swap(a,b);
	}
	return a;
}
int main()
{
	int T,TC;
	cin >> TC;
	string str;
	for(T=1;T<=TC;T++) {
		cout << "Case #" << T << ": "; 
		cin >> str;
		int index = str.find('/');
		int a,b;
		a = atoi(str.substr(0, index).c_str());
		b = atoi(str.substr(index+1, str.size()-index).c_str());
		int gcd = maxgcd(a,b);
		a = a/gcd;
		b = b/gcd;
		int tmp = b;

		int count = 0;
		while(a < b) {
			count ++;
			if((b&1) == 1) {
				cout << "impossible" << endl;
				break;
			}
			b = b>>1;
		}
		if(a<b)continue;
		while(b != 1) {
			if((b&1) == 1) {
				cout << "impossible" << endl;
				break;
			}
			b = b>>1;
		}
		if(b == 1)
			cout << count << endl;
	}
	return 0;
}