#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cctype>
#include <memory.h>
#include <vector>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <iomanip>

using namespace std;



int main()
{
    cin.tie(NULL);
    std::ios_base::sync_with_stdio(0);
    int t;
    fstream in;
    in.open ("//Users//Roman//Desktop//Contest//B.txt", std::fstream::in);
    in >> t;
    cout<<t;
    fstream out;
    out.open ("test.txt", std::fstream::in | std::fstream::out | std::fstream::app);
    for (int tt = 0; tt < t; ++tt){
        int ans = -1;
        int m;
        in >> m;
        vector < int > cakes (m);
        for (int i = 0; i < cakes.size(); ++i) {
            int a;
            in >> a;
            if (a > ans) {
                ans = a;
            }
            cakes[i] = a;
        }
        m = ans;
        for(int min = 1; min <= m; ++min) {
            vector < int > temp = cakes;
            int cur = 0;
            int steps = 0;
            while (min + steps < ans && cur < temp.size() ) {
                if (min >= temp[cur])
                {
                    cur++;
                }
                else
                {
                    int a = temp[cur] - min;
                    temp[cur] = a;
                    steps++;
                }
            }
            if (min + steps < ans) {
                ans = min + steps;
            }
        }
        out << "Case #" << tt + 1 << ": "<< ans << endl;
    }
    out.close();
    return 0;
}



