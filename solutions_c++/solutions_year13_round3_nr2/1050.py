/* BEGIN_OF_SOURCE_CODE */
#include <iostream>
#include <fstream>
#include <sstream>  

#include <cstring> //for memset
#include <cstdio>
#include <cmath>

#include <algorithm>
#include <numeric>
#include <iterator>

#include <vector>
#include <list>
#include <string>

#include <queue>
#include <stack>

#include <utility>
#include <map>
#include <set>
#include <iomanip> //??

#define REP(i,n) for(int i=0;i<(n);++i) 

using namespace std; //change 

int T;
int x, y;
string result;
string res;
bool finished;

void gao(int depth, int cx, int cy) {
    if(depth >= 500) return ;
    if(finished) return ;
    if(cx == x && cy == y) {
        finished = true;
        res = result.substr(0, depth + 1);
        return ;
    }
    int new_depth = depth+1;
    result[depth] = 'E'; gao(new_depth, cx+new_depth, cy);
    result[depth] = 'W'; gao(new_depth, cx-new_depth, cy);
    result[depth] = 'N'; gao(new_depth, cx, cy+new_depth);
    result[depth] = 'S'; gao(new_depth, cx, cy-new_depth);
    return ;
}

int main(void) {
    cin>>T;
    result.resize(500) ;
    for(int i = 1; i <= T; ++i) {
        cin>>x>>y;
        cout<<"Case #"<<i<<": ";
        string rr;

        if(x >= 0) {
            for(int i = 0; i < x; ++i) {
                rr += "WE";
            }
        }
        else {
            x = abs(x);
            for(int i = 0; i < x; ++i) {
                rr += "EW";
            }
        }

        if(y >= 0) {
            for(int i = 0; i < y; ++i) {
                rr += "SN";
            }
        }
        else {
            y = abs(y);
            for(int i = 0; i < y; ++i) {
                rr += "NS";
            }
        }
        cout<<rr<<endl;
    }

    return 0;
}
/* @END_OF_SOURCE_CODE */
