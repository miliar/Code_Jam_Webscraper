#include <fstream>
#include <vector>
#include <climits>

using namespace std;

ifstream cin("A-large.in");
ofstream cout("ans.txt");

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        long long n, x = 0;
        cin >> n;

        vector<bool> a(10);
        bool test;

        for (int i = 1; i < 1000; i++)
        {
            x += n, test = 1;

            string s;
            char buf[30] = "\0";
            s = itoa(x, buf, 10);

            for (int i = 0; i < 10; i++)
                if (a[i] == 1 || (s.find('0' + i) + 1))
                    a[i] = 1;
                else
                    test = 0;

            if (test)
                break;
        }

        if (test)
            cout << "Case #" << i + 1 << ": " << x << endl;
        else
            cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
    }

    return 0;
}
