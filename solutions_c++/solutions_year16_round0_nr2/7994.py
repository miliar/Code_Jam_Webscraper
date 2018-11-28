#include <bits/stdc++.h>
typedef long long int llu;
using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tt;
	char a[1000],prev;
	cin >> tt;
	for(int i=1; i<=tt; ++i){
		int ans = 0;
		scanf("%s",a);
		if(a[0] == '-'){
			prev = '-';
			ans = 1;
		}
		else if(a[0] == '+'){
			prev = '+';
			ans = 0;
		}
		for(int j=1; j<(int)strlen(a); ++j){
			if(a[j] != prev && a[j] == '-'){
				ans += 2;
			}
			prev = a[j];
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
