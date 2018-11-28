#include <iostream>
#include <cstdio>

using namespace std;

int a[10];

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, TT = 0;
    int n, i, tmp, s;
    
    cin >> T;
    for (TT = 1; TT <= T; TT++) {
	cin >> n;
	for (i = 0; i < 10; i++) 
	    a[i] = 0;
	
	s = 10;
	for (i = 1; s && n; i++) {
	    for (tmp = i * n; tmp; tmp /= 10){
		if (a[tmp % 10] == 0) s--;
		a[tmp % 10] = 1;
	    }
	}
	
	if (n == 0) printf("Case #%d: INSOMNIA\n", TT);
	else printf("Case #%d: %d\n", TT, (i - 1) * n);
    }
    return 0;
}
