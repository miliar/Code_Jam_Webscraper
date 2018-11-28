#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        string s;
        cin>>s;
        deque<char>d;
        d.push_back(s[0]);
        for(int i=1;i<(int)s.size();i++){
            deque<char>l,r;
            l=d;
            r=d;
            l.push_front(s[i]);
            r.push_back(s[i]);
            if(l>r)d=l;
            else d=r;
        }
        string ans(d.begin(),d.end());
        cout<<"Case #"<<z<<": "<<ans<<"\n";
    }
    return 0;
}
