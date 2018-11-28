#include<iostream>
using namespace std;

int div[20];
int getDiv(long long n) {
    for(long long i = 2; i*i <= n; i++) {
        if(n%i == 0) return i;
    }
    return 0;
}
int temp[50];
long long convert(int n, int base) {
    long long ans = 0;
    int i = 0;
    while(n) {
        temp[i++] = n%2;
        n /= 2;
    }
    for(int j = i-1; j >= 0; j--) {
        ans = ans*base+temp[j];
    }
    return ans;
}

int main() {
    int T;
//    T = 1;
    cin >> T;
    cout << "Case #1:\n";
    int N, J;
//    N = 16; J = 50;
    cin >> N >> J;
    int cnt = 0;
    for(int i = (1<<N-1)+1; i < (1<<N) && cnt < J; i+=2) {
        bool ok = true;
        long long converted;
        int t = getDiv(i);
        if(t) div[2] = t;
        else ok = false;
        for(int base = 3; base <= 10 && ok; base++) {
            converted = convert(i, base);
            t = getDiv(converted);
            if(t) div[base] = t;
            else {
                ok = false;
                break;
            }
        }
        if(ok) {
            cout << converted << " ";
            for(int i = 2; i <= 10; i++) {
                cout << div[i] << " ";
            }
            cout << "\n";
            cnt++;
        }
    }
}
