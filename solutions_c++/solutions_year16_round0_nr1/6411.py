#include <iostream>
#include <cstring>

using namespace std;

typedef long long ll;

ll solve(int n){
	if(n == 0) return -1;

	int dig = 0;
	ll counter = 1;

	while((dig & 1023) != 1023){
		ll temp = n * counter++;
		while(temp != 0){
			int t = temp % 10;
			dig |= 1 << t;
			temp /= 10;
		}
	}

	return n * counter - n;
}

int main(){
	int R;
	cin >> R;
	for(int i = 0; i < R; i++){
		int n;
		cin >> n;
		ll ans = solve(n);
		if(ans != -1)
			cout << "Case #" << i+1 << ": " << ans << endl;
		else
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
	}
	return 0;
}
