#include <iostream>
#include <set>
#include <string>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		int a;
		scanf("%d", &a);
		if(a == 0)
			printf("INSOMNIA\n");
		else {
			set<char> s;
			int k;
			for(k = a; ; k += a) {
				string s1 = to_string(k);
				for(auto& c : s1)
					s.insert(c);
				if(s.size() == 10)
					break;
			}
			printf("%d\n", k);
		}

	}
}