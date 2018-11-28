#include <iostream>
#include <string>
#include <set>

using namespace std;

int main ()
{
    int T;
    cin >> T;
    for (int k = 1; k <= T; ++ k)
    {
        int l, x;
        cin >> l >> x;
        string s;
        string ijk;
        cin >> s;
        bool flag = 0;
        while (x --)
            ijk += s;
        int c = 0;
        bool sign = 0;
        char act = '1';
        for (int i = 0; i < ijk.size (); ++ i)
        {
            if (act == '1')
            {
                act = ijk [i];
            }
            else if (act == 'i')
            {
                if (ijk [i] == 'i')
                {
                    act = '1';
                    sign = !sign;
                }
                else if (ijk [i] == 'j')
                {
                    act = 'k';
                }
                else if (ijk [i] == 'k')
                {
                    act = 'j';
                    sign = !sign;
                }
            }
            else if (act == 'j')
            {
                if (ijk [i] == 'i')
                {
                    act = 'k';
                    sign = !sign;
                }
                else if (ijk [i] == 'j')
                {
                    act = '1';
                    sign = !sign;
                }
                else if (ijk [i] == 'k')
                {
                    act = 'i';
                }
            }
            else if (act == 'k')
            {
                if (ijk [i] == 'i')
                {
                    act = 'j';
                }
                else if (ijk [i] == 'j')
                {
                    act = 'i';
                    sign = !sign;
                }
                else if (ijk [i] == 'k')
                {
                    act = '1';
                    sign = !sign;
                }
            }
            if (act == 'i' && !sign)
            {
                int j;
                act = '1';
                for (j = i+1; j < ijk.size (); ++ j)
                {
                    if (act == '1')
                    {
                        act = ijk [j];
                    }
                    else if (act == 'i')
                    {
                        if (ijk [j] == 'i')
                        {
                            act = '1';
                            sign = !sign;
                        }
                        else if (ijk [j] == 'j')
                        {
                            act = 'k';
                        }
                        else if (ijk [j] == 'k')
                        {
                            act = 'j';
                            sign = !sign;
                        }
                    }
                    else if (act == 'j')
                    {
                        if (ijk [j] == 'i')
                        {
                            act = 'k';
                            sign = !sign;
                        }
                        else if (ijk [j] == 'j')
                        {
                            act = '1';
                            sign = !sign;
                        }
                        else if (ijk [j] == 'k')
                        {
                            act = 'i';
                        }
                    }
                    else if (act == 'k')
                    {
                        if (ijk [j] == 'i')
                        {
                            act = 'j';
                        }
                        else if (ijk [j] == 'j')
                        {
                            act = 'i';
                            sign = !sign;
                        }
                        else if (ijk [j] == 'k')
                        {
                            act = '1';
                            sign = !sign;
                        }
                    }
                    if (act == 'j' && !sign)
                    {
                        break;
                    }
                }
                act = '1';
                for (j = j+1; j < ijk.size (); ++ j)
                {
                    if (act == '1')
                    {
                        act = ijk [j];
                    }
                    else if (act == 'i')
                    {
                        if (ijk [j] == 'i')
                        {
                            act = '1';
                            sign = !sign;
                        }
                        else if (ijk [j] == 'j')
                        {
                            act = 'k';
                        }
                        else if (ijk [j] == 'k')
                        {
                            act = 'j';
                            sign = !sign;
                        }
                    }
                    else if (act == 'j')
                    {
                        if (ijk [j] == 'i')
                        {
                            act = 'k';
                            sign = !sign;
                        }
                        else if (ijk [j] == 'j')
                        {
                            act = '1';
                            sign = !sign;
                        }
                        else if (ijk [j] == 'k')
                        {
                            act = 'i';
                        }
                    }
                    else if (act == 'k')
                    {
                        if (ijk [j] == 'i')
                        {
                            act = 'j';
                        }
                        else if (ijk [j] == 'j')
                        {
                            act = 'i';
                            sign = !sign;
                        }
                        else if (ijk [j] == 'k')
                        {
                            act = '1';
                            sign = !sign;
                        }
                    }
                }
                if (act == 'k' && !sign)
                {
                    flag = 1;
                    break;
                }
                act = 'i';
                sign = 0;
            }
        }
        cout << "Case #" << k << ": ";
        if (flag) cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}

