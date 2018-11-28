#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

int t,ans;
long long a,b;
int c[100];

bool check(int x){
	int len = 0;
	while (x != 0){
		len ++;
		c[len] = x % 10;
		x = x / 10;
	}
	for (int i = 1; i <= len / 2; i++){
		if (c[i] != c[len - i + 1]) return false;
	}
	return true;
}

int main(){

	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	scanf("%d", &t);
	for (int z = 1; z <= t; z++){
		cin >> a >> b;
		a = ceil(sqrt(a));
		b = floor(sqrt(b));
		ans = 0;
		for (int i = a; i <= b; i++){
			if (check(i) && check(i * i)) ans++;
		}
		printf("Case #%d: ", z);
		printf("%d\n", ans);
	}
	
	return 0;

}
