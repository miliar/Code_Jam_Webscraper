#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>

using namespace::std;

bool is_sum_zero(vector <int>& v)
{
    int sum = 0;
    for (int i = 0; i < v.size(); i++)
    {
        sum += v[i];
        if (sum != 0)
            return false;
    }

    return true;
}

void vector_fill(vector <int>& v, int n)
{
    while (n != 0)
    {
        int r = n % 10;
        if (v[r] == 1)
            v[r] = 0;
        n /= 10;
    }
}

int main()
{
    int T; cin >> T;
    for (int t = 1; t <= T; t++)
    {
        int n; cin >> n;
        if (n != 0)
        {
            vector <int> v(10, 1);
            int m = 0;
            while(!is_sum_zero(v))
            {
                m = m + n;
                vector_fill(v, m);
            }
            cout << "Case #" << t << ": " << m << endl;
        }
        else
            cout << "Case #" << t << ": INSOMNIA" << endl;
    }
}
