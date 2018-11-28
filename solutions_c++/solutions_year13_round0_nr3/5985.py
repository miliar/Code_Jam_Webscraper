#include <iostream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

bool is_palindrome(unsigned long long n)
{
    stringstream ss;
    ss << n;
    string s = ss.str();
    for (int i=0; i<s.length()/2; i++) {
        if (s[i] != s[s.length()-i-1])
            return false;
    }
    return true;
}

int main()
{
    unsigned T;
    cin >> T;
    for (unsigned t=1; t<=T; t++) {
        unsigned long long A, B;
        cin >> A >> B;
        unsigned long a = (unsigned long)(sqrt(A));
        unsigned long b = (unsigned long)(sqrt(B));
        while (a*a < A)
            a++;
        while (b*b > B)
            b--;
        unsigned count = 0;
        for (unsigned long long i=a; i<=b; i++) {
            if (is_palindrome(i) && is_palindrome(i*i))
                count++;
        }
        cout << "Case #" << t << ": " << count << endl;
    }
    return 0;
}
