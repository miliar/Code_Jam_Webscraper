#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tn;
    cin>>tn;
    for(int tc=1; tc<=tn; tc++)
    {
        int k, c, s;
        cin>>k>>c>>s;
        if((k+c-1)/c >s)
        {
            cout<<"Case #"<<tc<<": IMPOSSIBLE"<<endl;
            continue;
        }
        int n;
        for(n=k; n%c; n++);
        long long t=0;
        vector<long long> ans;
        for(int i=0; i<n; i++)
        {
            t*=k;
            if(i<k)
                t+=i;
            if((i+1)%c == 0)
            {
                ans.push_back(t+1);
                t=0;
            }
        }
        cout<<"Case #"<<tc<<": ";
            for(int i=0; i<ans.size(); i++)
                cout<<ans[i]<<" ";
            cout<<endl;
    }
    return 0;
}