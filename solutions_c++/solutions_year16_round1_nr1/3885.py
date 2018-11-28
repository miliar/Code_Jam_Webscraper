#include <iostream>
#include <algorithm>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <sstream>
using namespace std;

int main() {
    int ntc;
    cin>>ntc;
    for (int tc=1; tc<=ntc; ++tc) {
        string s;
        cin>>s;
        list<char> res;
        res.push_back(s[0]);
        for (int i=1; i<s.length(); ++i) {
            if (s[i]>=res.front()) res.push_front(s[i]);
            else res.push_back(s[i]);
        }
        ostringstream oss;
        for (auto i=res.begin(); i!=res.end(); ++i)
            oss<<*i;
        cout<<"Case #"<<tc<<": "<<oss.str()<<endl;
    }
    return 0;
}