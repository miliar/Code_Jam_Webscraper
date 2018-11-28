#include <iostream>

using namespace std;

void compute(int k, int c, int s)
{
    for(int i = 0; i < s; i++)
    {
        cout << ' ' << i+1;
    }
}

int main()
{
    int t, k, c, s;

    cin >> t;

    for(int i = 0; i < t; i++)
    {
        cin >> k >> c >> s;

        cout << "Case #" << i+1 << ":";
        compute(k, c, s);
        cout << endl;
    }

    return 0;
}
