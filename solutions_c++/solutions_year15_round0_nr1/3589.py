#include <iostream>
#include <map>
#include <string> 
#include <vector>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <queue>
#include <tuple>
#include <stack>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

using namespace std;

int main(int argc, const char * argv[]){
    int n, p, f;
    string s;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> p >> s;
        f = 0;

        int num = 0;
        int j = 0;
        while (num < p) {

            num += s[j] - '0';

            if (num <= j) {
                f++;
                num++;
            }
            j++;
            // cout << s[j]<<"|"<<j <<"|" << num << endl;
        }
        cout << "Case #" << i+1 << ": " << f << endl;


    }



    return 0;
}

