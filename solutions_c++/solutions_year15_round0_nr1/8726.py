#include <cassert>
#include <iostream>
#include <vector>
#include <map>
#include <cstdio>
#include <string>
#include <utility>
#include <algorithm>
#include <cmath>

using namespace std;


int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        int smax;
        cin >> smax;
        string str;
        cin >> str;
        int friends=0;
        int cur=0;
        if(smax>0) {
            for(int j=0; j<=smax; j++) {
                if(j>cur) {
                    friends+=(j-cur);
                    cur=j;
                }
                cur+=(str[j]-'0');
            }
        }

        cout << "Case #" << i << ": " << friends << endl;
    }
}
