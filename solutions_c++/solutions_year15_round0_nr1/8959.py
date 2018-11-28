#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{   freopen("a.in","r",stdin);
   freopen("a.txt","w",stdout);
    int t;
    int sm;
    string shy;
    int stood = 0;
    int req = 0;
    cin >> t;
    for(int i  = 1; i <= t; i++) {
        stood = 0;
        req = 0;
        cin >> sm >> shy;
        for(int j = 0; j <= sm; j++) {
            if(stood >= j) {
                stood += (shy[j] - '0');
            } else {
                req += (j - stood);
                stood += (j - stood);
                stood += (shy[j] - '0');
            }
        }
        cout << "Case #"<<i<<": "<<req << endl;
    }
    return 0;
}
