#include <vector>
#include <iomanip>
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


int lawn[101][101];

void func()
{
    int n,m;
    cin >> n >> m;
    memset(lawn, 0, sizeof(lawn));

    int max_num = 0;
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= m; ++j)
        {
            char c;
            cin >> c;
            lawn[i][j] = c - '0';
            max_num = max(max_num, c-'0'); 
        }
    }

    int flag = true;
    for (int i = 1; i <= n && flag; ++i)
        for (int j = 1; j <= m && flag; ++j)
        {
            int h_true = true;
            int v_true = true;
            int num = lawn[i][j];

            for (int r = 1; r <= n; ++r)
                if (lawn[r][j] > num)
                {
                    h_true = false;
                    break;
                }

            for (int c = 1; c <= m; ++c)
                if (lawn[i][c] > num)
                {
                    v_true = false;
                    break;
                }

            if (!h_true && !v_true)
                flag = false;
            else
                flag = true;
        }

    if (flag)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
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
