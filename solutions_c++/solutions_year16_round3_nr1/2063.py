#include <iostream>
#include <algorithm>
#include <set>
#include <string>
using namespace std;

int main()
{
    int T; cin>>T;
    for(int t=1; t<=T; ++t) {
        int n; cin>>n;
        vector<pair<int, int>> s;
        vector<int> v(n);
        int N=0;
        for(int i=0; i<n; ++i) {
            int a; cin>>a;
            s.emplace_back(a, i);
            N+=a;
            v[i]=a;
        }
        sort(s.rbegin(), s.rend());

        string res;
        if (N%2) {
            int c=s[0].second;
            res+=string(1, 'A'+c);
            res+=" ";
            --N;
            --v[c];
            --s[0].first;
            sort(s.rbegin(), s.rend());
        }
        while (N) {
            res+=string(1, char('A'+s[0].second));
            res+=string(1, char('A'+s[1].second));
            --v[s[0].second];
            --v[s[1].second];
            --s[0].first;
            --s[1].first;
            sort(s.rbegin(), s.rend());
            res+=" ";
            N-=2;
        }
        res.pop_back();
        cout<<"Case #"<<t<<": "<<res<<endl;
    }
}
