#include <fstream>

using namespace std;

ifstream cin ("B-small-attempt5.in");
ofstream cout ("b.txt");

string A[102][102];
int t, n, m, i, j, k, w, mi;

int main()
{
    cin >> t;
    for (i = 1; i <= t; ++i)
    {
        cin >> n >> m;
        for (j = 0; j < n; ++j)
        {
            for (k = 0; k < m; ++k)
            {
                cin >> A[j][k];
            }
        }
        bool res = 1;
        for (j = 0; j < n; ++j)
        {
            mi = 0;
            bool qwe = 1;
            for (k = 1; k < m; ++k)
            {
                if (A[j][k] != A[j][k - 1])
                    qwe = 0;
                if (A[j][mi] > A[j][k])
                    mi = k;
            }
            if (!qwe){
            for (k = 0; k < m; ++k)
            {
                if (A[j][k] == A[j][mi])
                {
                    for (w = 0; w < n; ++w)
                    {
                        if (A[w][k] > A[j][k])
                        {
                            w = n + 1;
                            j = n + 1;
                            k = m + 1;
                            res = 0;
                        }
                    }
                }
            }}
        }
        if (res)
            cout << "Case #" << i << ": YES" << endl;
        else
            cout << "Case #" << i << ": NO" << endl;
    }
}
