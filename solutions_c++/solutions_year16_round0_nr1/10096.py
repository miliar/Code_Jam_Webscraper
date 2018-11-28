#include <iostream>
#include <unordered_set>

using namespace std;
typedef unsigned long long ull;
int main()
{
    ull num, init, n;
    bool stop;
    cin >> n;
    unordered_set<ull> s;
    for (int i = 0; i < n; ++i)
    {
        int m = 1;
        unsigned int bs = 0u;
        s.clear();
        cin >> init;
        num = init;
        stop = false;
        ull lastn;
        while(s.count(num) == 0)
        {
            string ts = to_string(num);
            for (auto &c : ts)
                bs |= (1 << (c - '0'));
            if (bs == 1023)
            {
                stop = true;
                break;
            }
            s.insert(num);
            num = ++m*init;
            lastn = num;
        }

        cout << "Case #" << i+1 << ": ";
        if (stop)
            cout << lastn << std::endl;
        else
            cout << "INSOMNIA" << std::endl;

    }
    return 0;
}
