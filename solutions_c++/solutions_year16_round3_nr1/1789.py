#include<iostream>
#include<cstdio>
#include<cmath>
#include<math.h>
#include<cstring>
#include<string>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include <tuple>
using namespace std;

void init()
{
#ifdef MY_TEST_VAR
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
#endif
}

void solve()
{	
	unsigned n_cases = 0;
	scanf("%u", &n_cases);
	set<pair<unsigned, char>> results;
	for (unsigned T = 0; T < n_cases; ++T) {
		results.clear();
		unsigned n = 0;
		unsigned sum = 0;
		scanf("%u", &n);
		for (unsigned i = 0; i < n; ++i) {
			unsigned k = 0;
			scanf("%u", &k);
			sum += k;
			results.insert(make_pair(k, 'A' + i));
		}
		printf("Case #%u:", T + 1);
		if (sum % 2) {
			pair<unsigned, char> head = *results.rbegin();
			printf(" %c", head.second);
			results.erase(head);
			head.first -= 1;
			if (head.first > 0) {
				results.insert(head);
			}
			--sum;
		}
		for (unsigned i = 0; i < sum; i+= 2) {
			set<pair<unsigned, char>>::reverse_iterator it = results.rbegin();
			pair<unsigned, char> head1 = *it;
			++it;
			pair<unsigned, char> head2 = *it;
			printf(" %c%c", head1.second, head2.second);
			results.erase(head1);
			results.erase(head2);
			head1.first -= 1;
			if (head1.first > 0) {
				results.insert(head1);
			}
			head2.first -= 1;
			if (head2.first > 0) {
				results.insert(head2);
			}
		}
		printf("\n");
	}
}

int main()
{
	init();
	solve();
	return 0;
}