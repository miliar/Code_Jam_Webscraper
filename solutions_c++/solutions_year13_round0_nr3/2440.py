#include <vector>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <stack>
#include <map>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <string>
#include <set>

using namespace std;

#define DEBUG

#ifdef DEBUG
    #define debug(x...) msg(x);
#else
    #define debug(x...)
#endif

template <class t1>
void msg(t1 a)
{ cerr << a << endl; }
template <class t1, class t2>
void msg(t1 a, t2 b)
{ cerr << a << '\t' << b << endl; }
template <class t1, class t2, class t3>
void msg(t1 a, t2 b, t3 c)
{ cerr << a << '\t' << b << '\t' << c << endl; }
template <class t1, class t2, class t3, class t4>
void msg(t1 a, t2 b, t3 c, t4 d)
{ cerr << a << '\t' << b << '\t' << c << '\t' << d << endl; }
template <class t1, class t2, class t3, class t4, class t5>
void msg(t1 a, t2 b, t3 c, t4 d, t5 e)
{ cerr << a << '\t' << b << '\t' << c << '\t' << d << '\t' << e << endl; }
template <class t1, class t2, class t3, class t4, class t5, class t6>
void msg(t1 a, t2 b, t3 c, t4 d, t5 e, t6 f)
{ cerr << a << '\t' << b << '\t' << c << '\t' << d << '\t' << e << '\t' << f << endl; }

////////////////////////////////////////////////////////////////////////////
char str[200];
bool check(long long num)
{
    //memset(str, 0, sizeof(str));
    int  n = 0;
    while (num > 0)
    {
        str[n++] = num % 10;
        num /= 10;
    }

    int i = 0;
    int j = n-1;
    for (;i < j && str[i] == str[j]; ++i, --j)
        ;
    if (i < j)
        return false;
    else
        return true;
}

long long next_square(long long num)
{
    char buf[200] = { 0 };
    sprintf(buf, "%lld", num);
    int n = strlen(buf);
    int mid = 0;

    if ((n & 0x01) == 1)
        mid = n / 2;
    else
        mid = n / 2 - 1;

    int i;
    for (i = mid; i >= 0; --i)
    {
        if (buf[i] != '9')
        {
            buf[i]++;
            buf[n-1-i] = buf[i];
            for (int j = i+1; j < n-1-i; ++j)
                buf[j] = '0';
            break;
        }
    }

    if (i < 0)
    {
        buf[0] = '1';
        for (int i = 1; i <= n-1; ++i)
            buf[i] = '0';
        buf[n] = '1';
    }

    istringstream omes(buf);
    long long ret = 0;
    omes >> ret;
    return ret;
}

void func()
{
    long double n,m;
    cin >> n >> m;

    long long left = (long long)(sqrt(n) - 1);
    left = max((long long)0, left);
    long long right = (long long)(sqrt(m) + 1);

    long long i;
    for (i = left; i <= right && !check(i); ++i)
        ;

    int cnt = 0;
    for (; i <= right; i = next_square(i))
    {
        long long tmp = i * i;
        if (check(tmp) && tmp >= n && tmp <= m)
            cnt++;
    }

    cout << cnt << endl;
}


////////////////////////////////////////////////////////////////////////////

char in_file[] = "test.in";
char out_file[] = "test.out";

int main()
{
    int case_count, t;

    freopen(in_file, "r", stdin);
    freopen(out_file,"w", stdout);

    cin >> case_count;
    for (t = 1; t <= case_count; t++)
    {
        cerr << "\nDealing Case #" << t << endl;
        cout << "Case #" << t << ": ";
        func();
    }

	return 0;    
}
