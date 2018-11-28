#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int tick(int cur, vector<int>& p)
{
    int ret = cur;
    int d = p.size();

    for(int pi=0;pi<d;pi++)
    {
        if(p[pi] > cur)
        {
            if(p[pi] % cur == 0) ret += (p[pi]/cur-1);
            else ret += (p[pi]/cur);
        }
    }
    
    return ret;
}

int main()
{
    int cases;
    cin >> cases;

    for(int t=1;t<=cases;t++)
    {
        int d;
        cin >> d;
        vector<int> p;
        for(int pi=0;pi<d;pi++)
        {
            int pp;
            cin >> pp;
            p.push_back(pp);
        }

        sort(p.rbegin(), p.rend());

        int m = p[0];

        for(int i=1; i<m; i++)
        {
            m = min(tick(i, p), m);
        }


        cout << "Case #" << t << ": " << m << endl;
    }

    return 0;
}



