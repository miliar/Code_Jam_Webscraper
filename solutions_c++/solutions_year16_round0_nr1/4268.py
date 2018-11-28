#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
using namespace std;


int do_check(vector<int> &check, string nstr)
{
	for(int i=0; i<nstr.size(); ++i) {
		check[nstr[i] - '0'] = 1;
	}
	return 0;
}

int is_full(vector<int> &check)
{
	for(int i=0; i<check.size(); ++i) {
		if(check[i] == 0)
			return 0;
	}
	return 1;
}

int counting(int n)
{
	int cnt;
	int value = 0;

	vector<int> check(10);
	char valchr[100];

	while(1) {
		value = value + n;
		sprintf(valchr, "%d", value);
		do_check(check, valchr);
		if(is_full(check))
			return value;
	}
}

int main()
{
	int tcase, n;
	int result;

	scanf("%d" ,&tcase);

	for(int i=1; i<=tcase; ++i) {
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", i);
		}
		else {
			printf("Case #%d: %d\n", i, counting(n));
		}
	}
	return 0;
}
