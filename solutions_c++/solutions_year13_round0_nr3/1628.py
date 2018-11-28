#include <cstdio>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>

#define nPal 39

using namespace std;


long long pal[nPal] = {1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004
};

int cnt[10000000 + 10];

bool check_palindromes(long long x)
{
    stringstream ss;
    ss << x;
    string s;
    ss >> s;
    int len = s.length();
    for (int i=0; i<len/2; i++)
        if (s[i] != s[len-1-i])
            return false;
    return true;
}

void gen()
{
    cnt[0] = 0;
    for (long long i=1; i<=10000000; i++)
    {
        if (check_palindromes(i) && check_palindromes(i*i))
        {
            cout << i*i << endl;
        }
    }
}

void work()
{
    int T;
    long long A, B;
    cin >> T;
    for (int tim = 1; tim <= T; tim++)
    {
        cin >> A >> B;
        long long *lb = lower_bound(pal, pal+nPal, A);
        long long *ub = upper_bound(pal, pal+nPal, B);
        cout << "Case #" << tim << ": " << max(ub-lb, 0) << endl;
    }
}

int main()
{
    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.out", "w", stdout);
    work();
    return 0;
}
