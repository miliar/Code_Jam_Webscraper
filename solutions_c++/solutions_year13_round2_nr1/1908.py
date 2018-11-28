#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char * argv[])
{
    int nTests;
    ifstream in;
    in.open(argv[1]);
    ofstream out;
    out.open(argv[2]);
    in >> nTests;
    for (int tc = 0; tc < nTests; tc++)
    {
        out << "Case #" << tc + 1 << ": ";
        
        //cout << endl;
        vector<int> a, c;
        int n, size;
        in >> size >> n;
        if (size == 1)
        {
            a.resize(n);
            for (int i = 0; i < n; i++)
                in >> a[i];
            out << n << endl;
        }
        else
        {
            a.resize(n);
            c.resize(n);
            for (int i = 0; i < n; i++)
                in >> a[i];
            //cout << "Case #" << tc + 1 << ": ";
            //cout << "N = " << n << endl;
            //for (int i = 0; i < n; i++)
            //    cout << a[i] << " ";
            sort(a.begin(), a.end());
            int count = INT_MAX;
            for (int i = 0; i < n; i++)
            {
                if (i == 0)
                    c[i] = 0;
                else
                    c[i] = c[i - 1];
                if (a[i] < size)
                    size += a[i];
                else
                {
                    int t = size;
                    while (t <= a[i])
                    {
                        //cout << "here, i = " << i << ", t = " << t << "\n";
                        t += t - 1;
                        c[i]++;
                    }
                    size = t;
                    size += a[i];
                }
            }
            for (int i = 0; i < n; i++)
            {
                int m = min(n, c[i] + n - i - 1);
                if (m < count)
                    count = m;
            }
            out << count << endl;
        }
    }
}
