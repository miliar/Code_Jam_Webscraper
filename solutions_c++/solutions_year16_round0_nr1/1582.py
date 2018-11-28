#include <iostream>
#include <map>

using namespace std;

long long t, n, res;


long long calc(long long k) {
    bool histo[10] = {0};
    long long sum=0;
    if (k == 0)
        return -1;
    
    for (long long i = 1; ;i++) {
        long long z = i*k;
        while (z>0){
            if (histo[z%10] == 0) {
                histo[z%10] = 1;
                sum++;
            }
            z /= 10;
        }

        if (sum == 10)
            return i*k;
    }
    
}

int main() {
    cin >> t;

    for (long long i = 1; i <= t; i++) {
        cin >> n;
        res = calc(n);
        cout << "Case #"<< i<<": ";//<<(res == -1? "INSOMNIA" : res) << endl;
        if (res == -1)
            cout << "INSOMNIA" << endl;
        else
            cout << res << endl;
    }
    return 0;
}   
