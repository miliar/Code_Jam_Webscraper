#include <iostream>
using namespace std;
char s[1001], w[1001];
int smax;
int main(){
	int T, t, i, c, cs; cin >> T;
	//c: the clapping
	for (cs = 1; cs <= T; cs++){
		memset(s, 0, sizeof(s));
		cin >> smax >> s;
		if (!smax){ printf("Case #%d: %d\n", cs, 0); continue; }
		for (t = 0; t <= smax; t++)s[t] -= 0x30;
		/*cout << "debug:" << endl;
		for (t = 0; t <= smax; t++)printf("%d", s[t]);*/

		for (i = 0;; i++){
			memcpy(w, s, sizeof(s));
			w[0] += i; c = w[0];
			for (t = 1; t <= smax; t++){
				if (c >= t)c += w[t]; else break;
				if (t == smax){
					printf("Case #%d: %d\n", cs, i);
					goto nextcase;
				}
			}
		}
	nextcase:;
	}
	return 0;
}