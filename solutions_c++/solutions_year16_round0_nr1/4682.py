#include <iostream>
#include <vector>

using namespace std;

bool check(vector<int> &valid, long long N)
{
    int a;
    while (N > 0)
    {
        a = N % 10;
        if (valid[a] == 0)
            valid[a] = 1;
        N = N / 10;
    }
    bool ret = true;
    for (int i = 0; i < 10; i ++)
        if (valid[i] == 0)
            ret = false;
    return ret;
}

int main()
{
    int T;
    long long N;
    long long M;
    cin >> T;
    for (int t = 1; t <= T; t ++)
    {
        cout << "Case #" << t << ": ";
        cin >> N;
        vector<int> valid(10, 0);
        if (N <= 0)
        {
            cout << "INSOMNIA" << endl;
            continue;
        }
        for (int i = 0; i < 1000; i ++)
        {
            M = (i+1) * N;
            if (check(valid, M))
            {
                cout << M << endl;
                break;
            }
        }
    }
    return 0;
}
