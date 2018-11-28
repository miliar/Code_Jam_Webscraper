#include <bits/stdc++.h>

using namespace std;
bool flag;
int t, i, bk;
string s;

int get_ans()
{
    flag = !flag;
    if (flag)
    {
        while (bk>=0 && s[bk] == '+') bk--;
        if( bk>=0 ) return get_ans()+1;
        else return 0;
    }
    else
    {
        while (bk>=0 && s[bk] == '-') bk--;
        if( bk>=0 ) return get_ans()+1;
        else return 0;
    }
}

void solve()
{
    flag = 0;
    cin>>s; 
    bk = s.size()-1;
    cout<<"Case #"<<i<<": "<<get_ans()<<endl;
}

int main()
{
    cin>>t;
    for(i = 1; i<=t; i++)
    {
       solve();
    }
    return 0;
}
