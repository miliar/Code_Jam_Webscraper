#include <iostream>
#include <string>
#include <utility>
#include <cstddef>
#include <cassert>

using namespace std;

namespace
{
    using Val = size_t;

    inline char inv(char v)
    {
        switch(v)
        {
        case '-':
            return '+';
        case '+':
            return '-';
        default:
            assert(false);
            return v;
        }
    }

    pair<Val, bool> flips(const string &str, Val len)
    {
        auto cur(str);
        Val res = 0;
        while(true)
        {
            const auto p = cur.find_first_of('-');
            if(p == string::npos)
                break;
            if(cur.size() - p < len)
                return make_pair(0, false);
            for(Val i = 0; i < len; ++i)
                cur[p+i] = inv(cur[p+i]);
            ++res;
        }
        return make_pair(res, true);
    }
}

int main()
{
    int t = 0;
    cin>>t;
    string str;
    Val len = 0;
    for(int i = 0; i < t; ++i)
    {
        cin>>str>>len;
        const auto r = flips(str, len);
        cout<<"Case #"<<i+1<<": ";
        if(r.second)
            cout<<r.first;
        else
            cout<<"IMPOSSIBLE";
        cout<<endl;
    }
    return 0;
}
