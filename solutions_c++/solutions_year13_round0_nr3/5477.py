#include <iostream>
#include <cmath>

using namespace std;
int A, B;


static int reverseNum(int a) {
    int num = 0;
    while(a > 0) {
        int mod = a % 10;
        num *= 10;
        num += mod;
        a = a / 10;
    }
    
    return num;
}

static void solver(int t) {
    cout<< "Case #" << t << ": ";
    int count = 0;

    for (int i = A; i <= B; i++) {
        if (i % 10 == 0) {
            continue;
        }
        
        if (i == reverseNum(i)) {
            int a = sqrt(i);
            if (a * a == i && a == reverseNum(a)) {
                count++;
            }
        }
    }
    
    cout << count;
}



int main(int argc, const char * argv[])
{
    int T = 0;
    cin >> T;
    
    for (int t = 1; t <= T; t++) {
        cin >> A >> B;
        solver(t);
        cout << endl;
    }
    
    return 0;
}

