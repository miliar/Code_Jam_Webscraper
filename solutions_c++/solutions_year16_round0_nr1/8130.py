#include <iostream>
#include <string>
#include <set>
#include <sstream>

using namespace std;

int main()
{
    int t;
    int base;

    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i)
    {
        cin >> base;

        //cout << "TTTTTTTTTTTT " << base << endl;

        if (base == 0)
        {
            cout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }

        set<char> sc;
        int index = 1;
        int last = 0;
        while (true)
        {
            stringstream ss;
            last = base * index;
            ss << last;
            string s = ss.str();


            for (auto tItr = s.begin(); tItr != s.end(); tItr++)
            {
                //if (sc.count(*tItr) > 0)
                //cout << "aaa " << *tItr << endl;
                sc.insert(*tItr);
            }
            //            cout << s << " " << sc.size() << endl;
            if (sc.size() == 10)
            {
                break;
            }
            index++;
        }

        cout << "Case #" << i << ": " << last << endl;
    }

    return 0;
}
