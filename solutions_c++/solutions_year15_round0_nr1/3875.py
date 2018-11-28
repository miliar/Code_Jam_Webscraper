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
    cout << t;
    fstream out;
    out.open ("test.txt", std::fstream::in | std::fstream::out | std::fstream::app);
    for (int tt = 0; tt < t; ++tt){
        int ans = 0;
        int m;
        in >> m;
        string s;
        in >> s;
        vector < int > x(m + 1);
        for (int i = 0; i < x.size(); ++i) {
            x[i] = s[i] - '0';
        }
        int sum = x[0];
        for(int  i = 1; i < x.size(); ++i) {
            if (sum < i) {
                int dif = (i - sum);
                ans += dif;
                sum += dif;
            }
            sum += x[i];
        }
        out << "Case #" << tt + 1 << ": "<< ans << endl;
    }
    out.close();
    return 0;
}



