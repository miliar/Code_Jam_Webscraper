#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <limits>
#include <utility>
#include <cmath>
#include <string>

using namespace std;

bool isPalin(int x)
{
    ostringstream ss;
    ss << x;
    string s1 = ss.str();
    
    string s2 = s1;
    reverse(s2.begin(), s2.end());
    
    return s1 == s2;
}

int fairsquare()
{
    int A, B;
    cin >> A >> B;
    
//    cout << A << " " << B << endl;
    
    int count = 0;
    for (int i = static_cast<int>(sqrt(A)); i <= static_cast<int>(sqrt(B)) + 1; ++i) {
        int i2 = i * i;
        if (i2 >= A && i2 <= B && isPalin(i) && isPalin(i2))
            count++;
    }
    
    return count;
}

int main(int argc, char* argv[])
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t) {
        int output = fairsquare();

        cout << "Case #" << t + 1 << ": " << output << endl;
    }

    return 0;
}
