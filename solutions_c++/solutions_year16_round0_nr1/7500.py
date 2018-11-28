#include <bits/stdc++.h>
#define f first
#define s second
#define ll long long
#define mp make_pair
#define pb push_back
#define sqr(x) (x)*(x)

using namespace std;

double eps = 1e-9;
const int INF = 1e9+7;
const int MAXN = int (3e5+7);

int T, n, a[10];

bool check() {
	for(int i = 0; i < 10; i ++)
		if(!a[i])
			return 0;
	return 1;
}

void go(int x) {
	while(x) {
		a[x % 10] = 1;
		x /= 10;
 	}	
}

int main () { 
   	//freopen("input.in", "r", stdin);
   	//freopen("output.txt", "w", stdout);  
    
    cin >> T;
    for(int w = 0; w < T; w ++) {
    	cin >> n;
    	int add = n;
    	memset(a, 0, sizeof a);
    	if(n == 0) {
    		cout << "Case #" << w + 1 << ": INSOMNIA" << "\n";
    		continue;
    	}
    	go(n);
    	while(!check()) {
    		n += add;
    		go(n);
    	}
    	cout << "Case #" << w + 1 << ": " << n << "\n";
    }
    return 0;
} 