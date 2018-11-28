#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <sstream>

using namespace std;

typedef long long llong;

vector<pair<char, int> > V1, V2;

int main()
{
   // ios_base::sync_with_stdio(false);
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    
    int TC;
    cin>>TC;

    for(int j = 1; j <= TC; j++)
    {
        llong n;
        cin>>n;
        
        string a, b;
        cin>>a>>b;

        if(b.size() > a.size())
            swap(a,b);

        V1.clear();
        V2.clear();

        int it = 0;

        while(it < a.size())
        {
            char act = a[it];
            int cnt = 1;
        
            while(it + 1 < a.size() && a[it + 1] == act){
                cnt++;
                it++;
            }

            it++;

            V1.push_back(make_pair(act,cnt));
        }

        it = 0;

        while(it < b.size())
        {
            char act = b[it];
            int cnt = 1;

            while(it + 1 < b.size() && b[it + 1] == act){
                cnt++;
                it++;
            }

            it++;

            V2.push_back(make_pair(act,cnt));
        }

        if(V1.size() != V2.size()){
            printf("Case #%d: Fegla Won\n", j);
            continue;
        }

        bool cont = false;
        int ans = 0;

        for(int k = 0; k < V1.size(); k++)
        {
            if(V1[k].first == V2[k].first)
            {
                ans += max(V1[k].second, V2[k].second) - min(V1[k].second, V2[k].second);
            }
            else
            {
                printf("Case #%d: Fegla Won\n", j);
                cont = true;
                break;
            }
        }

        if(cont)
            continue;

        printf("Case #%d: %d\n", j, ans);
    }

    return 0;
}