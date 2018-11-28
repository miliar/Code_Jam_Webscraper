#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <random>
#include <set>
#include <sstream>
#include <cassert>

using namespace std;

typedef long long ll;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int T;
	cin >> T;
	for(int icase = 1;icase<=T;++icase){
		cout << "Case #" << icase << ": ";
		int a, b, k;
		int res = 0;
		cin >> a >> b >> k;
		for(int i=0;i<a;++i)
			for(int j=0;j<b;++j)
				if((i&j) < k)
					++res;
		cout << res << '\n';
	}
}