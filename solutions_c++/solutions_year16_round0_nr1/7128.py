#include <iostream>

using namespace std;



long int get_min_number(long int n)
{
    int a[10] = {0};
    int cnt = 0;
    for (int i = 1; ;++i)
    {
        long int r = n * i;
        while (r > 0)
        {
            int x = r % 10;
            if (a[x] == 0)
            {
                a[x] = 1;
                cnt++;
            }
            r /= 10;
        }
        if (cnt == 10)
        {
            return n * i;
        }
    }
    return 0;

} 



int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        int n;
        cin >> n;
        cout << "Case #" << i << ": " ;
        if (n == 0)
        {
            cout << "INSOMNIA";
        }
        else
        {
            cout << get_min_number(n);
        }
        cout << endl;
    }
    return 0;
}


