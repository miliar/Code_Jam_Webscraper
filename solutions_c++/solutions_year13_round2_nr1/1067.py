#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef pair<pair<long long, deque<long long> >, long long> pp;
int main()
{
    long long T;
    cin>>T;
    for(long long t=1;t<=T;t++) {
        long long r = INT_MAX;
        cout<<"Case #"<<t<<": ";
        long long A, N;
        cin>>A>>N;
        vector<long long> v(N);
        for(long long i=0;i<N;i++){
            cin>>v[i];
        }
        sort(v.begin(), v.end());
        deque<long long> qq(v.begin(), v.end());
        pp p;
        p.first.first = A;
        p.first.second= qq;
        p.second = 0;
        queue<pp > q;
        q.push(p);
        vector<deque<long long> > seen;
        while(!q.empty()) {
            p= q.front();
            q.pop();
            long long m = p.first.first;
            qq = p.first.second;
            long long l = p.second;
            while(!qq.empty() && m>qq.front()) {
                m += qq.front();
                qq.pop_front();
            }
            if(qq.empty()) {
                r = min(r, l);
            } else {
                qq.push_front(m-1);
                pp np;
                if(find(seen.begin(), seen.end(), qq)==seen.end()) {
                np.first.first = m;
                np.first.second = qq;
                np.second = l+1;
                q.push(np);
                seen.push_back(qq);
                }
                qq.pop_front();
                qq.pop_front();
                if(find(seen.begin(), seen.end(), qq)==seen.end()) {
                np.first.second = qq;
                q.push(np);
                seen.push_back(qq);
                }
            }
        }
        cout<<r<<endl;
       
    }

    return 0;
}
