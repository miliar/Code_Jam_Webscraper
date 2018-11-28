#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);

    ios::sync_with_stdio(0);
    int t; cin >> t;
    for(int test=1; test<=t; ++test)
    {
        long long ans=0; int n;
        vector<string> in;
        vector<int> perm;

        cin >> n;

        for(int i=1; i<=n; ++i)
            perm.push_back(i);

        for(int i=1; i<=n; ++i)
        {
            string tmp; cin >> tmp;
            in.push_back(tmp);
        }

        vector<int> chkng(256); int curr=0;

        do {
            string tmp=""; curr++;
            for(int i=0; i<n; ++i) tmp+= in[perm[i]-1];

            int chk=1;
            for(int i=0; i<tmp.size(); ++i)
            {
                if(chkng[tmp[i]]<curr)chkng[tmp[i]]=curr;
                else if(tmp[i]!=tmp[i-1]){chk=0; break;}
            }

            ans += chk;
        } while(next_permutation(perm.begin(), perm.end()));

        cout << "Case #" << test << ": " << ans << '\n';
    }
    return 0;
}
