#include <bits/stdc++.h>
#define lli long long int
#define s(x) scanf("%lld", &x)

using namespace std;

int visit[10];
lli no;

void doit()
{
	lli i,j,k;
	k = no;

	do {
		i = k % 10;
		k = k / 10;
		visit[i] = 1;
	} while(k);
}

bool check()
{
	lli i,j;

	j = 1;

	for (i = 0; i < 10; ++i) {
		if (visit[i] == 0)
			return false;
	}
	
	return true;
}

int main()
{
	lli tcase,i,j,k,ans,temp,tt,n2;

	s(tcase);
	tt = 1;

	while (tcase--) {
		printf("Case #%lld: ", tt);
		++tt;
		
		for (i = 0; i < 10; ++i)
			visit[i] = 0;

		s(no);
		n2 = no;

		if (no == 0) {
			printf("INSOMNIA\n");
			continue;
		}	
		
		j = 0;

		for (i = 1; i <= 500; ++i) {
			doit();
			if (check()) {
				j = 1;
				printf("%lld\n", no);
				break;
			}
			no += n2;
		}

		if (j == 0) {
			printf("INSOMNIA\n");
		}
	}

	return 0;
}
