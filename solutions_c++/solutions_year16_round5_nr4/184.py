#include<iostream>
#include<string>
using namespace std;

int main()
{
    int t, kase = 0;
    cin >> t;
    while (t--)
    {
        int n, l;
        cin >> n >> l;
        bool impossible = false;
        for (int i = 0; i < n; i++)
        {
            string str;
            cin >> str;
            bool valid = false;
            for (int j = 0; j < str.size(); j++)
                if (str[j] == '0')
                    valid = true;
            if (!valid) impossible = true;
        }
        string badString;
        cin >> badString;
        cout << "Case #" << ++kase << ": ";
        if (impossible)
        {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        string a = "0" + string(l - 1, '1');
        string b = "";
        for (int i = 0; i < l; i++)
            b += "0?";
        cout << a << " " << b << endl;
    }
    return 0;
}