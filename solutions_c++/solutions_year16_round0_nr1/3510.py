#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

const int XX = 1e7 + 10;

int cc[XX];
bool vis[XX];

int mask(int n){
	if (vis[n])	return cc[n];
	vis[n] = 1;
	int x = n;
	while (x){
		cc[n] |= 1<<(x % 10);
		x /= 10;
	}
	return cc[n];
}

int get(int n){
	int ms = mask(n), x = n;
	while (ms != 1023){
		x += n;
		ms |= mask(x);
	}
	return x;
}

int main(){
	int te;	cin >> te;
	for (int w = 1; w <= te; w++){
		int n;	cin >> n;
		cout << "Case #" << w << ": ";
		if (n == 0)
			cout << "INSOMNIA\n";
		else
			cout << get(n) << "\n";
	}
	return	0;
}
