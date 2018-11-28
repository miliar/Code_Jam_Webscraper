#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("Aout.txt", "w", stdout);
	int t; cin >> t;
	for(int tc=1; tc<=t; tc++){
		int n,x; cin >> n >> x;
		int a[n];
		int ans = 0;	
		for(int i = 0; i < n; i++){
			cin >> a[i];
		}
		sort(a, a+n);
		reverse(a, a+n);
		int used[n];
		memset(used, 0, sizeof used);
		for(int i = 0; i < n; i++){
//			cout << a[i] << endl;
			if(used[i]==0){
				used[i] = 1;
				int rem = x - a[i];
				for(int j = i+1; j < n; j++){
					if(used[j] == 1) continue;
					if(rem >= a[j]){
						used[j] = 1;
						break;
					}
				}
				ans++;
			}
		}
		if(ans > n){
			cout << " BLAH" << endl;
		}
		cout << "Case #" << tc <<": " << ans << endl;
		
	}
	return 0;
}
	
