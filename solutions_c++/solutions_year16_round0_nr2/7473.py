#include <iostream>
#include <string>
#include <cstdlib>
#include <bitset>

using namespace std;

bool check(string str, int len)
{
    bool c0 = true;
    bool c1 = true;

    for (int i = 0 ; i < len ; i++)
    {
        if (c0 == false && c1 == false)
            return false;

        if (str[i] == '0')
            c1 = false;
        else 
            c0 = false;
    }

    return c0 || c1;
}

int cal(string str, int len)
{
    int count = 0;
    int pos = len-2;
    char state = str[len-1];
   

    while (true)
    {
        if (check(str, len))
        {
            if (str[0] == '1')
                return count;
            else
                return count+1;
        }

        for (int i = pos ; i > -1 ; i--)
        {
            if (str[pos] == state)
            {
                pos--;
                continue;
            }

            if (str[pos] != str[0])
            {
                state = str[pos];
                pos--;
                break;
            }
        }

        //swap and count
        string newstr = "";
        for (int i = pos ; i > - 1 ; i--)
        {
            if (str[i] == '0')
                newstr.push_back('1');
            else
                newstr.push_back('0');
        }
        for (int i = pos+1 ; i < len ; i++)
            newstr.push_back(str[i]);

        state = str[len-1];
        pos = len-2;

        str = newstr;

        count++;
    }

    return -1;
}

int main()
{
    ios_base::sync_with_stdio(false);

    int t;
    string input;
    string ostr;

    cin >> t;

    for (int i = 0 ; i < t ; i++)
    {
        cin >> input;
        int len = input.length();
        ostr = "";
        int pos = 0;

        for (int j = 0 ; j < len ; j++)
        {
            if (input[j] == '-')
                input[j] = '0';
            else
                input[j] = '1';

            if (pos == 0)
            {
                pos++;
                ostr.push_back(input[j]);
            }
            else
            {
                if (ostr[pos-1] != input[j])
                {
                    pos++;
                    ostr.push_back(input[j]);
                }
            }
        }

        cout << "Case #" << i+1 << ": " << cal(ostr, ostr.length());

        if (i != t-1)
            cout << endl;
    }
}
