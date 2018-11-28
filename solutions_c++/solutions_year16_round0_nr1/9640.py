#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        long long n;
        cin >> n;
        if(n == 0) {
            cout << "Case #" << t << ": INSOMNIA\n";
        }
        else {
            set <int> s;
            for(long long i = 1; ; i++) {
                long long temp = i*n;
                while(temp) {
                    s.insert(temp % 10);
                    temp /= 10;
                }
                if(s.size() == 10) {
                    cout << "Case #" << t << ": " << i*n << "\n";
                    break;
                }
            }
        }
    }
    return 0;
}
