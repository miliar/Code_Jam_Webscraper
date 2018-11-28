#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
using namespace std;
bool SetDigets(set<int>& s, long long value)
{
    while(value)
    {
        s.insert(value % 10);
        value /= 10;
    }
    return s.size() == 10;
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        long long n;
        cin >> n;
        if (n == 0)
        {
            cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
        }
        else
        {
            set<int> s;
            long long k = 0;
            do 
            {
                ++k;
            } while(!SetDigets(s, k * n));
            cout << "Case #" << i + 1 << ": " << k * n << endl;
        }
    }
    return 0;
}