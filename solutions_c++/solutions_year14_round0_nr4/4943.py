#include <string>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <deque>
#include <set>
#include <cstdio>
#include <cstring>
#include <limits>

using namespace std;

int ww, wdw;
deque<double> wn, wk, wdn, wdk;

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int cases, boxes;
    scanf("%d", &cases);
    string line;
    for(int a = 1 ; a <= cases; ++a) {
        ww = 0, wdw = 0;
        wn.clear(); wk.clear(); wdn.clear(); wdk.clear();
        scanf("%d", &boxes);
        getline(cin, line);
        getline(cin, line);
        istringstream iss(line);
        double temp;
        while(iss >> temp) {
            //cout << temp << endl;
            wn.push_back(temp);
            wdn.push_back(temp);
        }
        getline(cin, line);
        iss.clear();
        iss.str(line);
        while(iss >> temp) {
            //cout << temp << endl;
            wk.push_back(temp);
            wdk.push_back(temp);
        }
        sort(wn.begin(), wn.end());
        sort(wk.begin(), wk.end());
        sort(wdn.begin(), wdn.end());
        sort(wdk.begin(), wdk.end());
        for(int i = wn.size()-1; i >= 0; --i) {
            for(int j = wn.size()-1; j >= 0; --j) {
                if(wk[i] > wn[j]) {
                    //cout << wk[i] << " " << wn[j] << endl;
                    ww++;
                    wn[j] = numeric_limits<double>::infinity();
                    break;
                }
            }
            if(wdn[wdn.size() - 1] > wdk[wdk.size() - 1]) {
                wdw++;
                wdn.pop_back();
                wdk.pop_back();
            } else /*if(wdn.size() != 0)*/{
                wdn.pop_front();
                wdk.pop_back();
            }
            //cout << wdn.size() << " " << wdk.size() << endl;
        }
        printf("Case #%d: %d %d\n", a, wdw, boxes - ww);
    }
    return 0;
}
