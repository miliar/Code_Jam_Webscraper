#include <cmath>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <functional>
using namespace std;

int main() {
    int ntc;
    cin>>ntc;
    for (int tc=1; tc<=ntc; ++tc) {
        int n, k, idx=0;
        cin>>n;
        priority_queue<pair<int, char>> q;
        for (int i=0; i<n; ++i) {
            cin>>k;
            q.push(make_pair(k, 'A'+(idx++))); 
        }
        cout<<"Case #"<<tc<<": ";
        while (!q.empty()) {
            pair<int, char> p=q.top();
            q.pop();
            cout<<p.second;
            if (p.first-1>0) q.push(make_pair(p.first-1, p.second));
            if (p.first==1 && !(q.size()%2)) {
                cout<<' ';
                continue;
            }
            if (!q.empty()) {
                pair<int, char> p=q.top();
                q.pop();
                cout<<p.second;
                if (p.first-1>0) q.push(make_pair(p.first-1, p.second));
            }
            cout<<' ';
        }
        cout<<'\n';
    }
    return 0;
}