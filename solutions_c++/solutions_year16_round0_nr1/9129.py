#include <bits/stdc++.h>
using namespace std;

vector<int> dig(10, 0);

void nums(long long int num) {
    
    while(num) {
        dig[num%10]++;
        num /= 10;
    }
}

bool checkVal() {
    for(int i = 0; i<10; ++i) {
        if(dig[i] == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        
        long long int n, m;
        cin >> n;
        if(n==0) {
            cout << "Case #" << i << ": INSOMNIA\n";
            fill(dig.begin(), dig.end(), 0);
            continue;
        }
        m = n;
        nums(m);
        while(checkVal() == false) {
            m += n;
            nums(m);
        }
        
        cout << "Case #" << i << ": " << m << endl;
        fill(dig.begin(), dig.end(), 0);
    }
    
	return 0;
}
