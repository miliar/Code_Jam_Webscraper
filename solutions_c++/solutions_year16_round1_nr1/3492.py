#include <iostream>
#include <string>
#include <climits>

using namespace std;

int main()
{
    int t;
    string s;
    cin >> t;
    cin.ignore();
    for (int a=1; a<=t; a++)
    {
        getline(cin, s);
        cout << "CASE #" << a << ": ";
        string str="";
        for (int i=0; i<s.length(); i++)
        {
            if (s[i]>=str[0])
            {
                str=s[i]+str;
            }
            else
            {
                str+=s[i];
            }
        }
        cout << str;
        cout << endl;
    }

    return 0;
}

