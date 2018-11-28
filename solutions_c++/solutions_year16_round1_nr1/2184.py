#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

int main(){
	int T,C,l;
	char s[1001];
	for (scanf("%d", &T), C = 1; C <= T; C++){
		printf("Case #%d: ", C);
		scanf("%s", s);
		string ans = "";
		ans+=s[0];
		l = strlen(s);
		for (int i = 1; i < l; i++){
			if (s[i] >= ans[0]) ans = s[i] + ans;
			else ans = ans + s[i];
		}
		cout<<ans<<endl;
	}
	return 0;
}
