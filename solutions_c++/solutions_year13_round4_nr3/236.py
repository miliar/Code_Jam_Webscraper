#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int a[2048];
int b[2048];

int x[2048];

int d[2048];

int na[2048];

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        int n;
        cin >> n;
        for (int i=0; i<n; i++)
            cin >> a[i];
        for (int i=0; i<n; i++)
            cin >> b[i];

        for (int i=0; i<n; i++)
        {
            d[i] = 0;
            x[i] = 0;
        }

        priority_queue<int, vector<int>, greater<int> > q;

        for (int i=0; i<n; i++)
        {
            if (a[i] == 1)
                d[i] |= 1;
            if (b[i] == 1)
                d[i] |= 2;
            if (d[i] == 3)
            {
                d[i] |= 4;
                q.push(i);
            }
        }

        for (int i=0; i<n; i++)
        {
            na[i] = n;

            for (int j=n-1; j>i; j--)
                if (a[j] == a[i])
                    na[i] = j;
        }


        for (int i=0; i<n; i++)
        {
            int t = q.top();
            q.pop();
            x[t] = i+1;

            for (int j=t+1; j<n; j++)
                if (a[j] == a[t] + 1)
                    d[j] |= 1;

            for (int j=0; j<t; j++)
                if (b[j] == b[t] + 1)
                    d[j] |= 2;

            for (int j=0; j<n; j++)
                if (d[j] == 3 && (na[j] == n || x[na[j]]))
                {
                    d[j] |= 4;
                    q.push(j);
                }
        }

        cout << "Case #" << tt << ":";

        for (int i=0; i<n; i++)
            cout << " " << x[i];
        cout << endl;

        for (int i=0; i<n; i++)
        {
            bool ok = false;

            for (int j=0; j<i; j++)
            {
                if (x[i] > x[j] && a[i] < a[j] + 1)
                    cout << ":(" << endl;
                if (x[i] > x[j] && a[i] == a[j] + 1)
                    ok = true;
            }

            if (!ok && a[i] > 1)
                cout << ":((" << endl;
        }

        for (int i=n-1; i>=0; i--)
        {
            bool ok = false;

            for (int j=n-1; j>i; j--)
            {
                if (x[i] > x[j] && b[i] < b[j] + 1)
                    cout << ":(" << endl;
                if (x[i] > x[j] && b[i] == b[j] + 1)
                    ok = true;
            }

            if (!ok && b[i] > 1)
                cout << ":,((" << " " << i << endl;
        }
    }
    return 0;
}
