#include <cstdio>
#include <iostream>
#include <algorithm>
#define ll long long int

using namespace std;

int main()
{
	int t;
	freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
	cin >> t;
	int k;
	for(k = 1; k <= t; k++) {
		int n;
		cin >> n;
		double a[10000];
		double b[10000];
		int mr[10000] = {0};
		int i;
		for(i = 0; i < n; i++) {
			cin >> a[i];
		}
		for(i = 0; i < n; i++) {
			cin >> b[i];
		}
		int j;
		int c = 0;
		sort(a,a+n);
		sort(b,b+n);
		
		for(i = 0; i <n; i++) {
			for(j = 0; j < n; j++) {
				if(b[j] > a[i] && mr[j] != -1)  {
					c++;
					mr[j] = -1;
					break;
				}
			}			
		}
		
		int m[10000] = {0};
		c = n - c;
		int c1 = 0;
		for(i = 1; i < n; i++) {
			for(j = 0; j < n; j++) {
				if(a[j] > b[i] && m[j] != -1) {
					c1++;
					m[j] = -1;
					break;
				}
			}
			
		}
		
		//cout << c1 << endl;
		for(i = 0; i < n; i++) {
			if(m[i] != -1 && b[0] < a[i]) {
				c1++;
				break;
			}
		}
		cout << "Case #" << k << ": ";
		cout << c1 << " " << c << endl;
		
		
	}
}
