#include <algorithm>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

struct rank_ {
    long long p, q;
    rank_(long long a, long long b)
    {
        p = a; q = b;
        for (long long x = 2; x * x <= a; ++x)
        {
            while ((p % x == 0) && (q % x == 0))
            {
                p /= x;
                q /= x;
            }
        }
        if (q % p == 0) {
            q /= p;
            p = 1;
        }
    }
};

int degree(long long k)
{
    long long i = 1;
    int count = 0;

    while (k > i)
    {
        i *= 2;
        count++;
    }

    if (k != i)
        return -1;
    else
        return count;
}

string solution(rank_ r)
{
    string bad = "impossible";
    if (r.p > r.q)
        return bad;
    
    int count = degree(r.q);

    if (count == -1)
        return bad;
    
    if (count > 40)
        return bad;

    if (r.p == 0)
        return bad;

    int ans = 0;
    while (2 * r.p < r.q) {
        ans++;
        r.p *= 2;
    }

    return to_string(ans + 1);
}

int main()
{
    ifstream cin("A-small-attempt0.in");
    ofstream cout("A-small-attempt0.out");
    
    int test_count;
    cin >> test_count;
    for (size_t test = 0; test < test_count; ++test)
    {
        long long a, b;
        char c;
        cin >> a >> c >> b;
        rank_ r(a, b);
        cout << "Case #" << to_string(test + 1) << ": " << solution(r) << endl;
    }

}
