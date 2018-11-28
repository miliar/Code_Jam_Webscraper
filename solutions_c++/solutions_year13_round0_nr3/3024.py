#include <iostream>
#include <algorithm>
#include <cstdlib>

bool isPallndromes(int);
bool isSquares(int);

using namespace std;

int main(){
	int n;
	int a,b;
	int ans;
	cin >> n;
	for(int i = 0; i < n; i++){
		ans = 0;
		cin >> a >> b;
		while(!(a > b)){
			if(isPallndromes(a) && isSquares(a)){
				ans++;
				//cout << ' ' << a << endl;
			}
			a++;
		}
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}

// 回文
bool isPallndromes(int a){
	int temp = a;
	int rev = 0;
	while(a > 0){
		rev *= 10;
		rev += a % 10;
		a /= 10;
	}
	if(temp % 10 == 0) rev *= 10;
	// cout << 'r' << rev << endl;
	if(temp == rev) return true;
	else return false;
}

bool isSquares(int a){
	for(int i = 1; i * i <= a; i++){
		if(i * i == a){
			if(isPallndromes(i)){
				return true;
			}
			return false;
		
		}
	}
	return false;
}


