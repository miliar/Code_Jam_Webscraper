#include <bits/stdc++.h>
using namespace std;

vector<int> arr(10, 0);

void digex(long long int n) {
    
    while(n) {
        arr[n%10]++;
        n /= 10;
    }
}

bool chck() {
    for(int i = 0; i<10; ++i) {
        if(arr[i] == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    
    freopen("inputt.txt", "r", stdin);//redirects standard input
    freopen("output.txt", "w", stdout);//redirects standard output
    
    long long int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        
        long long int n, m;
        cin >> n;
        if(n==0) {
            cout << "Case #" << i << ": INSOMNIA\n";
            fill(arr.begin(), arr.end(), 0);
            continue;
        }
        m = n;
        digex(m);
        while(chck() == false) {
            m += n;
            digex(m);
        }
        
        cout << "Case #" << i << ": " << m << endl;
        fill(arr.begin(), arr.end(), 0);
    }
    
	return 0;
}
