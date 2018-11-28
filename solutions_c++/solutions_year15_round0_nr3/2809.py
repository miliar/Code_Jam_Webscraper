#include <iostream>
#include <vector>
#include <cassert>
using namespace std;
int t;
int used = 0;
int xom, r, c;

class Quat
{
    char c;
    bool pos;
public:
    Quat(char C = '1', bool Pos = true): c(C), pos(Pos) {}
    bool operator==(const Quat& q) const
    {
        return c == q.c && pos == q.pos;
    }
    Quat operator*(const Quat& q) const
    {
        char resc;
        char respos = !(pos ^ q.pos);
        if (c == '1')
        {
            return Quat(q.c, respos);
        }
        if (c == 'i')
        {
            switch(q.c)
            {
                case '1':
                    resc = 'i';
                    break;
                case 'i':
                    resc = '1';
                    respos = !respos;
                    break;
                case 'j':
                    resc = 'k';
                    break;
                case 'k':
                    resc = 'j';
                    respos = !respos;
                    break;
            }
        }
        else if (c == 'j')
        {
            switch(q.c)
            {
                case '1':
                    resc = 'j';
                    break;
                case 'i':
                    resc = 'k';
                    respos = !respos;
                    break;
                case 'j':
                    resc = '1';
                    respos = !respos;
                    break;
                case 'k':
                    resc = 'i';
                    break;
            }
        }
        else if (c == 'k')
        {
            switch(q.c)
            {
                case '1':
                    resc = 'k';
                    break;
                case 'i':
                    resc = 'j';
                    break;
                case 'j':
                    resc = 'i';
                    respos = !respos;
                    break;
                case 'k':
                    resc = '1';
                    respos = !respos;
                    break;
            }
        }
        return Quat(resc, respos);
    }
    Quat operator/(const Quat& q) const
    {
        char resc;
        char respos = !(pos ^ q.pos);
        if (c == '1')
        {
            if (q.c != '1')
                respos = !respos;
            return Quat(q.c, respos);
        }
        if (c == 'i')
        {
            switch(q.c)
            {
                case '1':
                    resc = 'i';
                    break;
                case 'i':
                    resc = '1';
                    break;
                case 'j':
                    resc = 'k';
                    respos = !respos;
                    break;
                case 'k':
                    resc = 'j';
                    break;
            }
        }
        else if (c == 'j')
        {
            switch(q.c)
            {
                case '1':
                    resc = 'j';
                    break;
                case 'i':
                    resc = 'k';
                    break;
                case 'j':
                    resc = '1';
                    break;
                case 'k':
                    resc = 'i';
                    respos = !respos;
                    break;
            }
        }
        else if (c == 'k')
        {
            switch(q.c)
            {
                case '1':
                    resc = 'k';
                    break;
                case 'i':
                    resc = 'j';
                    respos = !respos;
                    break;
                case 'j':
                    resc = 'i';
                    break;
                case 'k':
                    resc = '1';
                    break;
            }
        }
        return Quat(resc, respos);
    }
};

void solve(int t)
{
    bool res = false;
    int l, x;
    string tmp, s;
    cin >> l >> x >> tmp;
    for(int i = 0; i < x; ++i)
        s += tmp;
    vector<Quat> be(s.size()), en(s.size());
    be[0] = s[0];
    en[s.size() - 1] = s[s.size() - 1];
    vector<int>pi, pk;
    Quat qj('j'), qi('i'), qk('k');
    
    if(be[0] == qi)
        pi.push_back(0);
    if(en[s.size()-1] == qk)
        pk.push_back(s.size() - 1);
    for (int i = 1; i < s.size(); ++i)
    {
        be[i] = be[i - 1] * Quat(s[i]);
        if (be[i] == qi)
            pi.push_back(i);
    }
    for (int i = (int)s.size() - 2; i >= 0; --i)
    {
        en[i] = Quat(s[i]) * en[i + 1];
        if (en[i] == qk)
            pk.push_back(i);
    }
    int pos = 0;
    for(int i = 0; i < pi.size(); ++i)
    {
        int j = 0;
        while(j < pk.size() && pi[i] + 1 < pk[j] )
        {
            if (en[pi[i] + 1] / en[pk[j]] == qj)
            {
                res = true;
                i = pi.size();
                break;
            }
            ++j;
        }
    }
    cout << "Case #" << t << ": " << (res ? "YES" : "NO") << endl;
}

int main()
{
    cin >> t;
    for(int i = 1; i <= t; ++i)
        solve(i);
}

