#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

void work()
{
	int ra, rb, x;
	set<int> a, b;
	cin >> ra;
	for (int i = 1; i <= 4; ++i)
		for (int j = 1; j <= 4; ++j) {			
			cin >> x;
			if (i == ra)
				a.insert(x);
		}
	cin >> rb;
	for (int i = 1; i <= 4; ++i)
		for (int j = 1; j <= 4; ++j) {
			cin >> x;
			if (i == rb && a.find(x) != a.end())
				b.insert(x);
		}
	if (b.empty())
		printf("Volunteer cheated!");
	else
	if (b.size() > 1)
		printf("Bad magician!");
	else
		printf("%d", *(b.begin()));	
}

int main()
{
    freopen("a1.in", "r", stdin);
    freopen("a1.out", "w", stdout);

    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);
        work();
        printf("\n");
    }
    
    return 0;
}
