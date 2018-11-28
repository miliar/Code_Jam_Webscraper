#include <bits/stdc++.h>

using namespace std;

string val;

bool alP(int lt)
{
    bool ft = true;
    for(int ct = 0; ct <= lt; ct++)
    {
        if(val[ct] == '-')
        {
            ft = false;
            break;
        }
    }
    return ft;
}

bool alN(int lt)
{
    bool ft = true;
    for(int ct = 0; ct <= lt; ct++)
    {
        if(val[ct] == '+')
        {
            ft = false;
            break;
        }
    }
    return ft;
}

long long get(int lt)
{
    if(alP(lt))
        return 0;
    if(alN(lt))
        return 1;

    if(lt < 0)
        return 0;
    if(lt == 0)
    {
        return val[lt] == '+' ? 0 : 1;
    }
    if(val[lt] == '+')
        return get(lt-1);
    else
    {
        while(val[lt] == '-')
            lt--;
        return get(lt) + 2;
    }
}

int main()
{
    int tetC;
    cin >> tetC;
    for(int cnt = 0; cnt < tetC; cnt++)
    {

        cin >> val;
        cout << "Case #"<<cnt+1<<": ";

        cout << get(val.size() -1) << endl;
    }
}
