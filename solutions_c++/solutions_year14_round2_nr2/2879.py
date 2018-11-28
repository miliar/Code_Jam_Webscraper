#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        int A, B, K;
        cin >> A >> B >> K;
        int sum=0;
        for (int j = 0; j < A; ++j)
            for (int k = 0; k < B; ++k) {
                if ((j & k) < K) {++sum;}
            }
        cout << "Case #" << i+1 << ": " << sum << endl;
    }
}
