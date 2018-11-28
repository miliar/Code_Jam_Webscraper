#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

char a[200];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);

	int task; scanf("%d", &task);
	for (int cs=1; cs<=task; cs++){
		scanf("%s", a);
		int p = 0, m = 0;
		for (int i=0; a[i]; i++){
			if (a[i]=='+'){
				m = p+1;
			}else{
				p = m+1;
			}
		}

		printf("Case #%d: %d\n", cs, p);
	}

	return 0;
}
