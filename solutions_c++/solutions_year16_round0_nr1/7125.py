#include <iostream>
#include <set>
#define lli long long int
using namespace std;

set<int> set1;

bool insert_digits(lli);

int main()
{
    int t;
    cin >> t;
    int case1 = 0;
    while(t--)
    {
        set1.clear();
        case1++;
        lli n;
        cin >> n;
        if (n == 0)
        {
            cout << "Case #" << case1 << ": " << "INSOMNIA" << endl;
            continue;
        }

        for (int i = 1; ; ++i )
        {
            lli res = n * i;
            bool res1 = insert_digits(res);
            if (res1)
            {
                cout << "Case #" << case1 << ": " << res << endl;
                break;
            }
        }


    }
    return 0;
}

bool insert_digits(lli res)
{
    while (res > 0)
    {
        set1.insert(res%10);
        res = res/10;
    }
    return (set1.size() == 10);
}
