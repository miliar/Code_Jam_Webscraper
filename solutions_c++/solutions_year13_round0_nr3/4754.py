#include <vector>
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

bool check(long long num)
{
    ostringstream mess;
    mess << num;

    string &str = mess.str();
    int len = len(str);
    int i = 0;
    int j = len-1;
    for (;i < j && str[i] == str[j]; ++i, --j)
        ;
    if (i < j)
        return false;
    else
        return true;
}

void func()
{
    long double n,m;
    cin >> n >> m;

    long long left = (long long)(sqrt(n) - 1);
    left = max(0, left);
    long long right = (long long)(sqrt(m) + 1);

    int cnt = 0;
    for (long long i = left; i <= right; ++i)
    {
        long long tmp = i * i;
        if (check(i) && tmp >= n && tmp <= m && check(tmp))
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
