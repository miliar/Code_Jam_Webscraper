#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>




using namespace std;

long long rev(long long x)
{
    long long ret = 0;
    while (x != 0)
    {
        ret *= 10;
        ret += (x%10);


        x /= 10;
    }

    return ret;
}

map<long long, long long> dyn;


int main()
{
    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);
    int nbT;
    cin >> nbT;
    long long pow10[16];
    pow10[0] = 1;
    for (int i = 1; i < 16; i++)
        pow10[i] = 10*pow10[i-1];

    priority_queue<pair<long long, long long>> toDo;
    //toDo.clear();
    toDo.push(make_pair(0,0));
    //cout << "orofhrhozoh" << toDo.size() << endl;
    while (!toDo.empty())
    {

        pair<long long, long long> cur = toDo.top();
        //cout << cur.second << "=>" << cur.first << endl;
        //cout << cur.first<< ",,," << cur.second << endl;
        toDo.pop();
        if (dyn.find(cur.second) != dyn.end())
            continue;

        dyn[cur.second] = cur.first;

        if (cur.second <= pow10[6])
        {
            if (dyn.find(cur.second+1) == dyn.end())
            {
              //  cout << "bli" << cur.second<< endl;
                //cout << "=>" << -cur.first+1 << endl;
                toDo.push(make_pair(cur.first-1, cur.second+1));
            }

            const long long revCur = rev(cur.second);
            if (revCur <= pow10[6] && dyn.find(revCur) == dyn.end())
            {
                //cout << "zaaaa" << cur.first+1 << endl;
                toDo.push(make_pair(cur.first-1,revCur));
            }
        }

    }
    for (int t = 1; t <= nbT; t++)
    {
        cout << "Case #" << t << ": ";

        long long N;
        cin >> N;

        long long rep = -1;
        if (dyn.find(N) != dyn.end())
            rep = dyn[N];
        rep = -rep;

        //cout << x << endl;
        cout << rep << '\n';

    }


    return 0;
}
