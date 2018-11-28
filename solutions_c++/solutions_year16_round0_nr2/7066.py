#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef unsigned long long ull;

int main() {
    freopen("/Users/vivekp/Downloads/B-large.in", "r", stdin);
    freopen("/Users/vivekp/Desktop/output", "w", stdout);
    int tc;
    cin>>tc;
    string cakes;
    for (int i = 1;i <= tc;i++) {
        cin>>cakes;
        int len = cakes.length();
        if(len == 1){
            if(cakes.at(0) == '+')
                cout<<"Case #"<<i<<": 0"<<endl;                
            else
                cout<<"Case #"<<i<<": 1"<<endl;
            continue;
        }
        int cnt = 0,groupEnd = 0,flipMid = 0,flipCnt = 0; 
        char prevC = '0';
        bool gotGroup = false,allPve = true; 
        while(cnt < len){
            char c = cakes.at(cnt);
            allPve = (c == '-')?false:allPve;
            prevC = (cnt == 0)?c:prevC;
            if(prevC != c){
                int tempCnt = cnt;
                flipMid = cnt;
                gotGroup = true;
                char nextGrpC = c;
                // travers to next dif symbol
                while(nextGrpC == c && cnt+1 < len){
                    cnt++;
                    nextGrpC = cakes.at(cnt);
                }
                if(nextGrpC != c)
                    groupEnd = cnt-1;
                else
                    groupEnd = len-1;

                // perform flips
                if(prevC == '+' && c == '-'){
                    // flip first portion of group
                    string f(flipMid,'-');
                    cakes.replace(0,flipMid,f);

                    // flip whole group
                    string f1(groupEnd+1,'+');
                    cakes.replace(0,groupEnd+1,f1);
                    flipCnt += 2;
                }else if(prevC == '-' && c == '+'){
                    // flip first portion of group
                    string f(flipMid,'+');
                    cakes.replace(0,flipMid,f);
                    flipCnt++;
                }
                // reset prev char to +, since all are changed to + ve
                prevC = '+';
                cnt = tempCnt-1;
            }
            cnt++;
        }
        if(!gotGroup){ // 1 or 0 flip required
            if(allPve)
                cout<<"Case #"<<i<<": "<<0<<endl; 
            else
                cout<<"Case #"<<i<<": "<<1<<endl;         
        }else{
            cout<<"Case #"<<i<<": "<<flipCnt<<endl;
        }
    }
    return 0;
}




