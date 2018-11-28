#include <iostream>

using namespace std;

int a[1<<20];

int main()
{
    int t;
    cin >> t;

    for (int tt=1; tt<=t; tt++)
    {
        int n, p, q, r, s;
        cin >> n >> p >> q >> r >> s;

        long long t = 0;

        for (long long i=0; i<n; i++)
            t += a[i] = (i * p + q) % r + s;

        long long s1 = 0, s2 = 0, s3 = t;

        long long m = t;

        for (int i=0, j=0; i<n; i++)
        {
            for (; s2 < s3 && j < n; j++)
            {
                s3 -= a[j];
                s2 += a[j];
                m = min(m, max(max(s1, s2), s3));
            }
            if (j > i)
            {
                j--;
                s3 += a[j];
                s2 -= a[j];
                m = min(m, max(max(s1, s2), s3));
            }

            if (j == i)
            {
                s3 -= a[j];
                s2 += a[j];
                j++;
                m = min(m, max(max(s1, s2), s3));
            }

            s1 += a[i];
            s2 -= a[i];
            m = min(m, max(max(s1, s2), s3));
        }

        cout.setf(ios::fixed);
        cout.precision(12);
        cout << "Case #" << tt << ": " << (double)(t - m) / t << endl;
    }
    return 0;
}
