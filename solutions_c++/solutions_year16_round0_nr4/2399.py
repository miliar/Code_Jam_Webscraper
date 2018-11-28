#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[])
{

	if (argc == 2) {
		freopen(argv[1], "r", stdin);
	} else if (argc == 3) {
		freopen(argv[1], "r", stdin);
		freopen(argv[2], "w", stdout);
	}

	int T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		int k,c,s;
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d: ", ++cas);
		for(int i=1;i<=s;i++) printf("%d%c",i,i==s?'\n':' ');
	}
	return 0;
}