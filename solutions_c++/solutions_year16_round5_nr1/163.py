#include <vector>
#include <iostream>
using namespace std;
int main() {
    int tt;
    cin>>tt;
    for(int xx = 1; xx <= tt; ++xx) {
        cout<<"Case #"<<xx<<": ";
        string s;
        cin>>s;
        vector<int> v;
        int sum = 0;
        int n = s.size();
        for(int i = 0; i < n; ++i) {
            if(n-i == v.size()) {
                if(v.back() == s[i]) sum += 10;
                else sum += 5;
                v.pop_back();
            }
            else {
                if(v.size() && v.back() == s[i]) {
                    sum += 10;
                    v.pop_back();
                }
                else {
                    v.push_back(s[i]);
                }
            }
        }
        cout<<sum<<'\n';

    }
}
