#include <bits/stdc++.h> 

#define ll long long
#define ull unsigned long long
#define md 1000000007LL
#define EPS 0.0000000001
#define INF 1LL << 40
#define next(i) ((i) + ((i) & (-i))) 
#define prev(i) ((i) - ((i) & (-i)))


using namespace std;

int main() {
#ifndef ONLINE_JUDGE 
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    //freopen("plane-tickets.in", "r", stdin);
    //freopen("plane-tickets.out", "w", stdout);
#endif // DEBUG
    srand(time(NULL));

    int t;
    cin >> t;

    for (int i = 0; i < t; i++) 
    {
        string s;
        cin >> s;
        reverse(s.begin(), s.end());
        char cur = '+';
        int k = 0;
        
        for (int i = 0; i < (int)s.size(); i++) 
        {
            if (s[i] != cur) 
            {
                k++;
                cur = s[i];
            }
        }

        cout << "Case #" << i + 1 << ": " << k << endl;
    }


    fprintf(stderr, "Execution time = %.4lfsec", (double)clock() / (double)CLOCKS_PER_SEC);
    return 0;
}
