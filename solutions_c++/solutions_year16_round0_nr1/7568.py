#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

bool exist[10];
int a[10], b[10];
int n, T;

bool checkAllHappen(){
	for (int i=0; i<10; i++)
		if (!exist[i]) return false;
	return true;
}

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	cin >> T;
	for (int h=1; h<=T; h++){
		cin >> n;
		cout << "Case #" << h << ": ";
		if (n == 0) {cout << "INSOMNIA" << endl; continue;}
		
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		memset(exist, false, sizeof(exist));
		b[0] = 0;
		while (n > 0){
			b[++b[0]] = n % 10;
			n /= 10;
		}
		while (!checkAllHappen()){
			for (int i=1; i<=max(a[0], b[0]); i++){
				a[i+1] += (a[i] + b[i]) / 10;
				a[i] = (a[i] + b[i]) % 10;
				exist[a[i]] = true;
			}
			a[0] = max(a[0], b[0]);
			if (a[a[0]+1] != 0) {a[0]++; exist[a[a[0]]] = true;}
		}
		for (int i=a[0]; i>=1; i--) cout << a[i];
		cout << endl;
	}
	return 0;
}
