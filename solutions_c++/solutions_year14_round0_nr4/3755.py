#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <vector>
#include <cassert>

using namespace std;

typedef long double ld;

int main(int argc, char* argv[])
{
    (void)argv; (void)argc;
    FILE* useless;
    cin.precision(10);
    useless=freopen("D-large.in", "r", stdin);
    useless=freopen("D-large.out", "w", stdout);
    assert(useless!=NULL);
    int t;
    cin >> t;
    for(int maiusato=1; maiusato<=t; maiusato++)
    {
        int n;
        ld temp;
        cin >> n;
        vector<ld> val[2];
        vector<ld> val2[2];
        for(int i=0; i<2; i++)
        {
            for(int j=0; j<n; j++)
            {
                cin >> temp;
                val[i].push_back(temp);
                val2[i].push_back(temp);
            }
        }
        int war=0, unfairWar=0;
        for(int i=0; i<2; i++)
        {
            sort(val[i].begin(), val[i].end());
            sort(val2[i].begin(), val2[i].end());
        }
        for(int i=0; i<(int)val[0].size(); i++)
        {
            vector<ld>::iterator it=lower_bound(val[1].begin(), val[1].end(), val[0][i]);
            if(it==val[1].end())
            {
                war++;
                val[1].erase(val[1].begin());
            }
            else
            {
                val[1].erase(it);
            }
        }
        /*if(maiusato==4)
        {
            for(int i=0; i<2; i++)
            {
                cout << "Vettore " << i+1 << ": ";
                for(int j=0; j<(int)val2[i].size(); j++)
                {
                    cout << val2[i][j] << " ";
                }
                cout << endl;
            }
        }*/
        for(int i=0; i<(int)val2[0].size(); i++)
        {
            if(val2[0][i]>val2[1][0])
            {
                unfairWar++;
                val2[1].erase(val2[1].begin());
            }
            else
            {
                val2[1].pop_back();
            }
        }
        cout << "Case #" << maiusato << ": " << unfairWar << " " << war;
        if(maiusato!=t)
            cout << endl;
        val[0].clear();
        val[1].clear();
    }
    return 0;
}
