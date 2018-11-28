#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

void solveTest(const int &testNumber)
{
    long long unsigned int r,t;
    cin >> r;
    cin >> t;

    double D = (1.0-2.0*(double)r)*(1.0-2.0*(double)r) + (t*8.0);
    double a = ((1.0-2.0*(double)r) + sqrt(D))/4.0;
    long long unsigned int ans = static_cast<long long unsigned int>(a);

    long long unsigned int s = ans*(2*(ans+r)-1);
    if(s > t) --ans;
    cout << "Case #" << testNumber << ": " << ans << endl;
}

int main(int argc, char* argv[])
{
    int T; cin >> T;
    for(int i = 0; i < T; ++i)
    {
        solveTest(i+1);
    }
    return 0;
}

