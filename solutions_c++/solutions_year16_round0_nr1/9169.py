#include <bits/stdc++.h> 

#define ll long long
#define ull unsigned long long
#define md 1000000007LL
#define EPS 0.0000000001
#define INF 1LL << 40
#define next(i) ((i) + ((i) & (-i))) 
#define prev(i) ((i) - ((i) & (-i)))


using namespace std;

vector<bool> dif(int x) 
{
    vector<bool> ans = vector<bool> (10, false);

    while (x > 0) 
    {
        ans[x % 10] = true;
        x /= 10;
    }
    
    return ans;
}


int naive(int n) 
{
    vector<bool> f = vector<bool> (10, false);
    int k = 0;

    int cur = 0;
    while (k < 10) 
    {
        cur++;
        vector<bool> now = dif(cur * n);
        for (int i = 0; i < 10; i++) 
        {
            if (f[i] == false && now[i] == true) 
            {
                k++;
                f[i] = true;
            }
        }


        if (cur > 1000000)
        {
            break;
        }
    }

    return cur;
}



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
        int x;
        cin >> x;
        if (x == 0) 
        {
            cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
        } else 
        {
            cout << "Case #" << i + 1 << ": " << 1ll * x * naive(x) << endl;
        }
    }


    fprintf(stderr, "Execution time = %.4lfsec", (double)clock() / (double)CLOCKS_PER_SEC);
    return 0;
}
