#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("q3.out", "w", stdout);
	int t, i, j, n, ans1, ans2, l = 1;
	double a;
	scanf("%d", &t);
	while(t--) {
		ans1 = ans2 = 0;
		scanf("%d", &n);
		list<double> arr1;
		list<double> arr2;
		list<double> arr3;
		for (i = 0; i < n; i++) {
			scanf("%lf", &a);
			arr1.push_back(a);	
		}
		for (i = 0; i < n; i++) {
			scanf("%lf", &a);
			arr2.push_back(a);
			arr3.push_back(a);
		}
		arr1.sort();
		arr2.sort();
		arr3.sort();
		list<double>::iterator itr1, itr2;
		itr1 = arr1.end();
		itr1--;
		for ( ; ; itr1--) {
			itr2 = arr2.end();
			itr2--;
			for ( ; ; itr2--) {
				if (*itr1 > *itr2) {
					arr2.remove(*itr2);
					ans1++;
					break;
				}
				if (itr2 == arr2.begin())
					break;
			}
			if (itr1 == arr1.begin())
				break;
		}
		for (itr1 = arr3.begin(); itr1 != arr3.end(); itr1++) {
			for (itr2 = arr1.begin(); itr2 != arr1.end(); itr2++) {
				if(*itr1 > *itr2) {
					arr1.remove(*itr2);
					ans2++;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n", l++, ans1, n - ans2);
	}
	return 0;
}
