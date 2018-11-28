#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

struct Number
{
    char c;
    int sign;

    public:
        Number(char c, int sign);
};

Number::Number(char c, int sign)
{
    this->c = c;
    this->sign = sign;
}

string s;
Number stringRes('1', 1);
Number prefRes('1', 1);

Number multiply(Number a, Number b)
{
    Number res('1', 1);
    res.sign = a.sign*b.sign;

    if(a.c == '1')
        res.c = b.c;
    else if(a.c == 'i')
    {
        if(b.c == '1') res.c = 'i';
        if(b.c == 'i') res.c = '1', res.sign*=-1;
        if(b.c == 'j') res.c = 'k';
        if(b.c == 'k') res.c = 'j', res.sign *= -1;
    }
    else if(a.c == 'j')
    {
        if(b.c == '1') res.c = 'j';
        if(b.c == 'i') res.c = 'k', res.sign*=-1;
        if(b.c == 'j') res.c = '1', res.sign*=-1;
        if(b.c == 'k') res.c = 'i';
    }
    else if(a.c == 'k')
    {
        if(b.c == '1') res.c = 'k';
        if(b.c == 'i') res.c = 'j';
        if(b.c == 'j') res.c = 'i', res.sign*=-1;
        if(b.c == 'k') res.c = '1', res.sign*=-1;
    }

    return res;
}

bool findLast()
{
    if(multiply(prefRes, Number('k', 1)).c == stringRes.c
       &&multiply(prefRes, Number('k', 1)).sign == stringRes.sign)
        return true;
    else
        return false;
}

bool findTwo(int start)
{
    Number curr('1', 1);

    bool res = false;
    for(int i=start; i<s.length(); i++)
    {
        curr = multiply(curr, Number(s[i], 1));
        prefRes = multiply(prefRes, Number(s[i], 1));
        if(curr.c == 'j' && curr.sign == 1)
            if(findLast())
                return true;
    }
    return false;
}

int main()
{
    int t;
    cin >> t;

    for(int k=1; k<=t; k++)
    {
        int l, x;
        cin >> l >> x;
        string tmp;
        cin >> tmp;
        s = "";

        while(x--)
            s += tmp;

        Number curr('1', 1);
        stringRes = Number('1', 1);
        prefRes = Number('1', 1);

        for(int i=0; i<s.length(); i++) stringRes = multiply(stringRes, Number(s[i], 1));

        bool res = false;
        for(int i=0; i<s.length(); i++)
        {
            curr = multiply(curr, Number(s[i], 1));
            prefRes = multiply(prefRes, Number(s[i], 1));
            if(curr.c == 'i' && curr.sign == 1)
            {
                if(findTwo(i+1))
                {
                    res = true;
                    break;
                }
                prefRes = curr;
            }
        }

        cout << "Case #" << k << ": ";
        if(res)
            cout << "YES\n";
        else
            cout << "NO\n";
    }

    return 0;
}
