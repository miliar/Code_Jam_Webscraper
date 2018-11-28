#include <iostream>
#include <string>

using namespace std;

string solve(long long n){
    bool bitmap[] = {
            false,//0
            false,//1
            false,//2
            false,//3
            false,//4
            false,//5
            false,//6
            false,//7
            false,//8
            false //9
    };
    int remain = 10;
    long long k, m = n;
    int i = 1;
    while(true) {
        k = m;
#if TRACE
        cout << k << " -> ";
#endif
        while(k > 0){
            int d = k % 10;
            if(bitmap[d] == false) {
#if TRACE
                cout << d << ", ";
#endif
                remain--;
                bitmap[d] = true;
            }
            k = k / 10;
        }
#if TRACE
        cout << " : " << remain << endl;
#endif
        if(remain == 0)
            break;

        i++;
        k = n * i;
        if(k == m)
            return "INSOMNIA";
        m = k;
    }
    return std::to_string(m);
}

int main() {
    int n;
    cin >> n;
    long long t;
    for (int i = 1; i <= n; i++) {
      cin >> t;
      string result = solve(t);
        cout << "Case #" << i << ": " << result << endl;
    }
    return 0;
}