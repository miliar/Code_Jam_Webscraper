#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <stdio.h>
#include <string>
#include <queue>
#include <iterator>

using namespace std;

int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);

    int T;

    cin >> T;

    for(int t = 0; t < T; ++t)
    {
        double C, F, X, A = 0;

        cin >> C >> F >> X;

        double ololo = 2, farm = 0;

        vector<double> data;

        data.push_back(X / ololo);

        int count = 0;

        bool ok = true;

        while(ok)
        {
            farm += C / ololo;
            ololo += F;
            data.push_back(farm + X / ololo);
            ++count;
            if(data[count] > data[count - 1])
                ok = false;
        }

        A = data[count - 1];

            
        printf("Case #%d: %.7f\n", t + 1, A);

    }

    return 0;
}