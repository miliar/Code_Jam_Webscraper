#include <iostream>
#include <set>

using namespace std;

set<char> getSet(long long num)
{
    set<char> ret;
    do{
        ret.insert('0' +(num%10));
        num = num/ 10;
    }while (num >0) ;
    return ret;
}

int main()
{
    std::ios::sync_with_stdio(false);
    int t,T;
    cin >> T;
    for (t=0; t<T; t++)
    {
        long long inp,cur;
        cin >> inp;
        cur =inp;
        string ans;
        set<char> target,curSet;
        for (int i=0; i<10; i++) {
            target.insert('0'+i);
        }
        if (inp == 0)
        {
            ans = "INSOMNIA";
        }
        else
        {
            curSet = getSet(cur);
            while (curSet != target)
            {
                cur += inp;
                set<char> nset = getSet(cur);
                for (set<char>::iterator si = nset.begin(); si != nset.end(); si++) {
                    curSet.insert(*si);
                }
            }
            ans = to_string(cur);
        }
        cout <<"Case #"<<t+1<<": "<<ans  <<endl;
    }
    return 0;
}

