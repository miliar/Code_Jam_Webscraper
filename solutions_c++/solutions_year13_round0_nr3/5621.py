#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;

bool is_square(int a) {
    return sqrt((double)a) - (int)sqrt((double)a) < 0.0001;
}

bool is_palindrome(int a) {
    stringstream inout;
    string intstr;
    inout << a;
    inout >> intstr;

    for (size_t i=0; i<intstr.length()/2; i++) {
        if (intstr[i] != intstr[intstr.length()-i-1]) return false;
    }

    return true;
}

int num_fair_and_squares(int min, int max) {
    int ret=0;
    for (int i=min; i<=max; i++) {
        if (is_square(i) && is_palindrome(i) && is_palindrome((int)sqrt((double)i))) ret++;
    }
    return ret;
}

int main()
{
    int T;
    cin >> T;

    for (int i=0; i<T; i++) {
        int A, B;
        cin >> A >> B;

        cout << "Case #" << (i+1) << ": " << num_fair_and_squares(A, B) << endl;
    }

    return 0;
}
