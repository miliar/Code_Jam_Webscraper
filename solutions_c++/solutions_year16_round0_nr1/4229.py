#include <bits/stdc++.h>
using namespace std;
#define lli unsigned long long int
lli track[10] = {0LL}; int c=0;

void count_nums(lli n){
	int tmp;
	while (n > 0){
		tmp = n % 10LL;
		n /= 10LL;
		if (!track[tmp]++) c++;
	}
}

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cases; cin >> cases; lli n;
	for (int i = 0; i < cases; i++){
		cin >> n;
		memset(track, 0LL, sizeof(track)); c=0;
		count_nums(n); cout << "Case #" << (i+1) << ": ";
		if (!n) cout << "INSOMNIA\n";
		else{
			for (int j = 2; true; j++){
				if (c == 10){
					cout << (n*(j-1)) << "\n";
					break;
				}
				count_nums(n * j);
			}
		}
	}
	return 0;
}