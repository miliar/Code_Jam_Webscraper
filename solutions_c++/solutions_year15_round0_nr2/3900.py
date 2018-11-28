#include <bits/stdc++.h>

using namespace std;

int bestmv;
void rec(vector<int> p, int nummv)
{
    if (nummv>=bestmv) return;
    sort(p.begin(), p.end());
    vector<int> o = p;
    // eat all
    if (nummv+p[p.size()-1]<=bestmv) bestmv = nummv+p[p.size()-1];
    // no special
    for (int i=0;i<p.size();i++) p[i] = max(0, p[i]-1);
    sort(p.begin(), p.end());
    if (p[p.size()-1]==0)
    {
        if (nummv+1<bestmv) bestmv = nummv+1;
    } else
    {
        rec(p, nummv+1);
    }
    // special
    int v = o[o.size()-1];
    for (int k=v-1;k>=1 && k>=v/2;k--)
    {
        if (nummv+1>=bestmv) break;
        p = o;
        p[p.size()-1] -= k;
        p.push_back(k);
        sort(p.begin(), p.end());
        rec(p, nummv+1);
    }
}

int main(int argc,char *argv[])
{
    int T;
    cin >> T;
    for (int t=0;t<T;t++)
    {
        int D;
        cin >> D;
        vector<int> p(D);
        for (int i=0;i<D;i++)
            cin >> p[i];
        sort(p.begin(), p.end());
        bestmv = p[p.size()-1];
        rec(p, 0);

        cout << "Case #" << t+1 << ": " << bestmv << endl;
    }

    return 0;
}
