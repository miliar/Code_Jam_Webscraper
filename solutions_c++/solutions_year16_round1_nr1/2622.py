#include <stdio.h>
#include <string.h>
#include <string>
char buf[2000];
using namespace std;
int main() {
	int __;
	scanf("%d",&__);
	for (int _ = 1; _ <= __; _++) {
		scanf("%s",buf);
		int l = strlen(buf);
		string s = "";
		for (int i = 0; i < l; i++)
			if (buf[i] >= s[0])
				s = buf[i] + s;
			else
				s += buf[i];
		printf("Case #%d: %s\n", _, s.c_str());
	}
	return 0;
}

