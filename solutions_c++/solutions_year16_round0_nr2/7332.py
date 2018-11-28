#include <iostream>
#include <string>
#include <algorithm>
#include <stack>

using namespace std;

void result()
{
    stack<char> a, b, c;

    string s;
    int len, st, i;
    char val;
    int count = 0;

    cin >> s;

    if(s.find('+') == -1)
    {
            cout << 1;              // if all contains -
    }
    else if(s.find('-') == -1)
    {
        cout << 0;              // if all contains +
    }
    else
    {

        for(i = 0; i < s.size(); i++)
            a.push(s[i]);

        len = s.size();
        st = b.size();

        while(st != len)
        {
            if(a.empty())
            {
                break;
            }
            else
            {
                val = a.top();

                while(a.top() == val)
                {
                    b.push(a.top());
                    a.pop();
                    val = b.top();

                    if(a.empty())
                        break;
                }

            }

            while(!(a.empty()))
            {
                c.push(a.top());
                a.pop();
            }

            while(!c.empty())
            {
                char ch = c.top();

                c.pop();

                if(ch == '+')
                    ch = '-';
                else if(ch == '-')
                    ch = '+';

                a.push(ch);

            }

            st = b.size();
            count++;
        }

        if(b.top() == '+')
            cout << count-1;
        else
            cout << count;
    }
}


int main()
{
    int test, i = 1;

    cin >> test;

    while(test--)
    {
        cout << "case #"<< i++ <<": ";

        result();

        cout << endl;
    }

return 0;
}
