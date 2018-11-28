#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <vector>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

void trim(vector<char>& v)
{
    bool bPos = true;

    for (auto tItr = v.rbegin(); tItr != v.rend(); tItr++)
    {
        if (bPos == true && *tItr == '+')
        {
            v.pop_back();
        }
        else if (bPos == true && *tItr == '-')
        {
           return;
        }
    }
}
void count(const vector<char>& v, int& move)
{
    if (v.size() == 1)
    {
        if (v[0] == '-')
        {
            move++;
        }
        return;
    }

    if (v.size() == 2)
    {
        //cout << "aa " <<move << " " << v[0]<<v[1]<<endl;
        if (v[0] == '-' && v[1] == '+')
        {
            move++;
        }
        else if (v[0] == '+' && v[1] == '-')
        {
            move += 2;
        }
        else if (v[0] == '+' && v[1] == '+')
        {

        }
        else
        {
            move++;
        }
    }
}
vector<char> flip(const vector<char>& v)
{
    vector<char> r;

    for (auto tItr = v.rbegin(); tItr != v.rend(); tItr++)
    {
        if (*tItr == '+')
        {
            r.push_back('-');
        }
        else
        {
            r.push_back('+');
        }
    }

    return r;
}
void dump(const vector<char>& v)
{
    for (auto c : v)
        cout << c;

        cout << endl;
}

int main()
{
    int t;
    string s;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i)
    {
        cin >> s;
        //cout << s << endl;

        int move = 0;
        vector<char> v;
        char last = 0;
        for (auto tItr = s.begin(); tItr != s.end(); tItr++)
        {
            if (last != *tItr)
            {
                last = *tItr;
                v.push_back(*tItr);
            }
        }

        trim(v);
        //dump(v);
        if (v.empty())
        {
            cout << "Case #" << i << ": " << move << endl;
            continue;
        }
        else if (v.size() == 1 || v.size() == 2)
        {
            count(v, move);
        }
        else
        {

            while(true)
            {
                vector<char> r = flip(v);
                move++;
                trim(r);

                //cout << "aaa " << move << " " << r.size();
                //dump(r);

                if (r.empty())
                {
                    break;
                }
                else if (r.size() == 1 || r.size() == 2)
                {
                    if (v == r)
                    {
                        move--;
                    }

                    count(r, move);
                    break;
                }
                else if (v ==r)
                {
                    move--;
                    move += v.size();
                    break;
                }
                v = r;
            }
        }

        cout << "Case #" << i << ": " << move << endl;
    }
    return 0;
}
