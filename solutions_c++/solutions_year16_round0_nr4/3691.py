#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

long long t, k, c, s, kpowc;
vector<long long> current_ans;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin>>t;
    for(int cs = 1; cs <= t; cs++)
    {
        cin>>k>>c>>s;


        if(k == 1)
        {
            cout<<"Case #"<<cs<<": "<<1<<endl;
            continue;
        }

        kpowc = 1;
        for(int i = 0; i < c; i++)
        {
            kpowc *= k;
        }

        for(unsigned long long j = 1; j <= kpowc; j += (
                                                        kpowc - 1) / (k - 1))
        {
            current_ans.push_back(j);
        }

        cout<<"Case #"<<cs<<":";
        for(int i = 0; i < current_ans.size(); i++)
        {
            cout<<" "<<current_ans[i];
        }

        if(current_ans.size() == 0) cout<<" Impossible";
        cout<<endl;

        current_ans.clear();
    }

    return 0;
}
