#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

map<char,bool> mapper;

int main() {
	
	int T;
	ll input;
	scanf("%d", &T);
	
	for (int i = 1; i <= T; i++) {
		scanf("%lld", &input);
		mapper = map<char,bool>();
		bool insomnia = false, end = false;
		string res = "", str = "";
		
		ll curN = 0;
		int count = 0;
		
		for (int fat = 1; ;fat++) {
			ll n = input * fat;
			
			if (n == curN) {
				insomnia = true;
				break;
			}
			
			stringstream ss;
			ss << n;
			ss >> str;
			
			int size = str.size();
			
			for (int j = 0; j < size; j++) {
				if ( !mapper[str[j]] ) {
					mapper[str[j]] = true;
					count++;
				
					if (count == 10) {
						res = str;
						end = true;
						break;
					}
				}
			}
			
			if (end) {
				break;
			}
		}
		
		if (insomnia) {
			printf("Case #%d: INSOMNIA\n", i);
		} else {
			printf("Case #%d: %s\n", i, res.c_str());
		}
	}
	
	return 0;
}