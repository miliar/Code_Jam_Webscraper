#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <cstdio>
#include <deque>

using namespace std;

int main()
{
    freopen("D://A-large.in", "r", stdin);
    freopen("D://A-large.out", "w", stdout);
    int T;
    cin>>T;

    for(int i=0; i<T; ++i){
        string s, res;
        cin>>s;
        deque<char> dc;
        dc.push_back(s[0]);
        for(int j=1; j<s.size(); ++j){
            if(s[j]>=dc[0]) dc.push_front(s[j]);
            else dc.push_back(s[j]);
        }
        for(int j=0; j<dc.size(); ++j){
            res.push_back(dc[j]);
        }
        cout<<"Case #"<<i+1<<": "<<res<<endl;
    }
    return 0;
}
