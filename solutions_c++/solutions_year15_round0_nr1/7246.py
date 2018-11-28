#include <iostream>
#include <string>

int main(void) {

    using namespace std;
    int T = 0;
    cin >> T;
    for(int i = 1; i <= T; i++) {
        int smax;
        cin >> smax;
        string str;
        cin >> str;
        int a = 0;
        int cur = 0;
        for(int j = 0; j <= smax; j++) {
            int add = (cur < j) ? j-cur:0;
            int sj = str.at(j) - '0';
            a += add;
            cur += sj + add;
        }
        cout << "Case #" << i << ": " << a << endl;
    }
    


    return 0;
}
