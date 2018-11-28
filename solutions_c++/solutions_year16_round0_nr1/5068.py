#include <bits/stdc++.h>

using namespace std;

int main() {

	int n, t, count = 1;

	scanf("%d", &t);
	while(t--) {
		scanf("%d", &n);
		if(n == 0)
			printf("Case #%d: INSOMNIA\n", count);
		else {
			long int number, i = 1, c = 0;
			vector<bool> v(10,false);
			string s;
			while(true) {
				s = s.append(to_string(i*n));
				for(int j = 0; j < s.size(); j++) {
					if(!v[s[j]-'0']) {
						v[s[j]-'0'] = true;
						c++;
					}
				}
				if(c == 10)
					break;
				i++;
			}
			printf("Case #%d: %ld\n", count, i*n);
		}
		count++;
	}

	return 0;
}