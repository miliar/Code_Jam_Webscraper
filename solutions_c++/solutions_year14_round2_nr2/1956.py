//#define LARGE
#define SMALL

#include <iostream>

using namespace std;

int it, tt;
int i, j, a, b, k, counter;

int main()
{
#if defined(LARGE)
    freopen("../B-large.in", "r", stdin);
    freopen("../B-large.out", "w", stdout);
#elif defined(SMALL)
    freopen("../B-small-attempt0.in", "r", stdin);
    freopen("../B-small.out", "w", stdout);
#else
    freopen("input.txt", "r", stdin);
#endif

    cin >> tt;

    for(it = 1; it <= tt; ++it)
    {
        cin >> a >> b >> k;

        counter = 0;
        for(i = 0; i < a; ++i)
        {
            for(j = 0; j < b; ++j)
            {
                if((i & j) < k) ++counter;
            }
        }

        cout << "Case #" << it << ": " << counter << endl;
    }

    return 0;
}

