#include <iostream>
#include <set>
using namespace std;
typedef multiset<int>::iterator sit;
int main() {
    int t;
    cin>>t;
    for(int tt = 0; tt < t; ++tt) {
        cout<<"Case #"<<tt+1<<": ";
        int n;
        int x;
        cin>>n>>x;
        multiset<int> st;
        for(int i = 0; i < n; ++i) {
            int q;
            cin>>q;
            st.insert(q);
        }
        int ans = 0;
        while(st.size()) {
            if(st.size() ==1) {
                ++ans;
                break;
            }
            int q = *st.begin();
            ++ans;
            st.erase(st.begin());
            int w = x - q;
            sit it = st.upper_bound(w);
            if(it != st.begin()){
                --it;
                st.erase(it);
            }
        }
        cout<<ans<<'\n';

    }
}
