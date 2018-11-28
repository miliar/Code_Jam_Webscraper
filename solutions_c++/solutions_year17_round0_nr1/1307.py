#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
    ios_base::sync_with_stdio(0);
    int T;
    cerr<<"------ start -----"<<endl;
    cin>>T;
    string s;
    for(int t = 1; t <= T; ++t)
    {
        cerr<<"----- "<< t<<" ------"<<'\n';
        int ans = 0, k, cur = 0;
        cin>>s>>k;

        int n = s.size();
        std::vector<int> v(n);
        {
            int i;
            for(i = 0; i <= n-k; ++i)
            {
                if(cur&1)
                {
                    if(s[i] == '-')s[i] = '+';
                    else s[i] = '-';
                }

                if(s[i] == '-')
                {
                    ++ans;
                    ++cur;
                    ++v[i+k-1];
                    s[i] = '+';
                }
                cerr<<cur<<' ';

                cur -= v[i];

            }

            for(; i < n; ++i)
            {
                if(cur&1)
                {
                    if(s[i] == '-')s[i] = '+';
                    else s[i] = '-';
                }
                cerr<<cur<<' ';

                cur -= v[i];

            }
        }
        bool is = true;

        cerr<<s << ' '<<ans <<endl;
        for(int i:v)
            cerr<<i;
        cerr<<'\n';

        for(char i : s)
            is = is && i == '+';

        cout<<"Case #"<<t<<": ";
        if(is)cout<< ans ;
        else cout<< "IMPOSSIBLE";
        cout<<'\n';
    }
    cerr<<"------ done -----"<<endl;
    return 0;
}
