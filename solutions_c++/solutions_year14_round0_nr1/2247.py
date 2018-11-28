#include <cstdio>
#include <iostream>
#define ll long long int

using namespace std;
int main()
{
	ll t;
	
	ll k, i, j, arr[6][6], brr[6][6], a, b, value;
	
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);
	
	cin >> t;	
	for (k = 1; k <= t; k++) {
		cin >> a;
		
		for (i = 1; i <= 4; i++) {
			for (j = 1; j <= 4; j++) {
				cin >> arr[i][j];
			}
		}
		
		cin >> b;
		
		for (i = 1; i <= 4; i++) {
			for (j = 1; j <= 4; j++) {
				cin >> brr[i][j];
			}
		}
		
		ll count = 0;
		
		for (i = 1; i <= 4; i++) {
			for (j = 1; j <= 4; j++) {
				if (arr[a][i] == brr[b][j]) {
					value = arr[a][i];
					count++;
				}
			}
		}
		
		if (count == 1) {
			printf("Case #%lld: %lld\n", k, value);
		}
		
		else if (count == 0) {
			printf("Case #%lld: Volunteer cheated!\n", k);
		}
		else if (count > 1) {
			printf("Case #%lld: Bad magician!\n", k);
		}
	}
	
	return 0;
}
