#include <iostream>
#include <string>

using namespace std;

typedef long long ll;


// Will need x^0 = 0
// look at length  ^ (K - 1) * 0 + 0 -> first guy
// look at length  ^ (C - 1) * 1 + 1 -> second guy
// look at length ^ (C - 1) * 2 + 2 -> third guy
// etc. etc

ll LazyPow(ll x, ll pow)
{
    if (pow == 0)
        return 0;
    
    ll ret = 1;
    
    while (pow--)
        ret *= x;
    
    return ret;
}

// 1 8
// After base increase:
// 0 for first, 
// Expect 1, 5, 9
// 0, it takes up 9, so start of second is at 9

// 1 8
// 1 16

// Ok
// 2, 2 leads to:
    // 1, 4 (0, 2)
    // 2 -> 2 ^ 1
// 2, 3 leads to:
    // 1, 8 (0, 6)
    // 6 -> 2 ^ 1 + 2 ^ 2
// 2, 4 leads to:
    // 1, 16 (0, 14)
    // 14 -> 2 ^ 1 + 2^ 2 + 2 ^ 3
// Like a shift of 2^(C) for the last (of course)

// 3, 2 leads to:
    // 1, 5, 9 (0, 3, 6)
// 3, 3 leads to:
    // 1, , 27 (0, 
int main()
{
    int T;
    cin >> T;
    
    for (int t = 1; t <= T; ++t)
    {
        // This will only work on the small dataset, has no change for the large
        int K, C, S;
        cin >> K >> C >> S;
        
        // Calculate how many are before its subgroup, then add i and one
        // Is based on C
        // Follow it down, instead of building it up
        ll baseIncrease = LazyPow(K, C - 1);
        ll offsetIncrease = baseIncrease / K; // Will be an integer
        cout << "Case #" << t << ":";
        for (int i = 0; i < K; ++i)
        {
            // numBefore = i
            // for C -1 steps:
            // numBefore = numBefore * K
            ll numBefore = i;
            for (int j = 0; j < C - 1; ++j)
                numBefore = numBefore * K + i;
            cout << ' ' << numBefore + 1;
        }
        cout << '\n';
    }
    
    // So, for 2, is 2, N - 1
}