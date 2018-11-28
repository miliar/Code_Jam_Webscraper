#include <iostream>

using namespace std;

int f(int n) {
    int reqMask = 0x3FF;
    int mask = 0;
    int i = 1;
    while(true) {
        int m = i*n;
        while(m > 0) {
            int rem = m%10;
            m /= 10;
            mask |= 1<<rem;
        }
        if(mask == reqMask) return i*n;
        i++;
    }
}

int main()
{
    int T;
    cin >> T;
    for(int caseno=1;caseno<=T;caseno++) {
        int n;
        cin >> n;
        if(n == 0) {
            cout << "Case #" << caseno << ": INSOMNIA" << endl;
        } else {
            cout << "Case #" << caseno << ": " << f(n) << endl;
        }
    }
}
