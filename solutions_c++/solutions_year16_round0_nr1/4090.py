#include <iostream>
#include <vector>
using namespace std;


bool check(vector<bool> &counter, int n)
{
    while (n > 0)
    {
        int d = n % 10;
        counter[d] = true;
        n /= 10;
    }

    for (int i = 0; i < 10; ++i)
    {
        if (!counter[i])
            return false;
    }
    return true;
}




int main()
{

    int t;

    cin >> t;

    vector<bool> counter;
    counter.reserve(10);




    for (int c = 1; c <= t; ++c)
    {
        int n;
        int multi = 1;
        cin >> n;

        counter.assign(10, false);

        if (n == 0)
        {
            cout << "Case #" << c << ": " << "INSOMNIA" << endl;
            continue;
        }

        while (!check(counter, n * multi))
        {
            multi++;
        }

        cout << "Case #" << c << ": " << n * multi << endl;
    }
    return 0;
}