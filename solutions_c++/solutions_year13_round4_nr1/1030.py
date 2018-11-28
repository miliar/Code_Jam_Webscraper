#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long lint;

int main()
{
    // freopen("a2.in", "r", stdin);
    // freopen("a2.out", "w", stdout);

    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);

        lint rint = 1000002013;

        int N, M;
        cin>>N>>M;

        map<int, lint> in;

        std::vector<lint> price;
        price.push_back(0);
        for (int i = 1; i <= N; ++i)
        {
            price.push_back(price[i-1]+N+1-i);
        }

        lint total = 0;
        for (int i = 0; i < M; ++i)
        {
            lint ii, o, p;
            cin>>ii>>o>>p;

            ii--;
            o--;

            if (in.find(ii) != in.end())
            {
                in[ii] = in[ii] + p;
            } else {
                in[ii] = p;
            }
            if (in.find(o) != in.end())
            {
                in[o] = in[o] - p;
            } else {
                in[o] = -p;
            }

            // cout<<ii<<" "<<in[ii]<<endl;
            // cout<<o<<" "<<in[o]<<endl;

            total += (price[o-ii]*p) % rint;
            total %= rint;
        }

        // for (map<int, lint>::iterator now = in.begin(); 
        //     now != in.end(); ++now)
        // {
        //     cout<<now->first<<" "<<now->second<<endl;
        // }
        
        lint real = 0;
        for (map<int, lint>::iterator down = in.begin(); down != in.end(); ++down)
        {

            map<int, lint>::iterator up = down;
            while(down->second<0){
                while(up->second <= 0) up --;
                
                lint p = min(-down->second, up->second);

                real += (price[down->first - up->first]*p) % rint;
                real %= rint;

                down->second += p;
                up->second -= p;
            }
        }

        cout<< (total - real + rint) % rint;

        printf("\n");
    }
    
    return 0;
}