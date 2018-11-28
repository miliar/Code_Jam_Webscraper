#include <iostream>
#include <string>
#include <vector>

using namespace std;

int ceil(int n, int d)
{
    int ans = n/d;
    if (n%d) ans++;
    return ans;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);

    int T;
    cin>>T;
    for (int cas=1; cas<=T; cas++)
    {
        int n;
        cin>>n;
        vector<int> d(n);
        for (int i=0; i<n; i++)
        {
            cin>>d[i];
        }
        int ans1=0;
        const int maxrate = 0;
        int rate=maxrate;
        for (int i=1; i<n; i++)
        {
            if (d[i-1]>d[i])
            {
                ans1+=d[i-1]-d[i];
                rate = max(rate, d[i-1]-d[i]);
            }
        }
        //cout<<"rate"<<rate<<endl;
        int ans2=0;
        for (int i=1; i<n; i++)
        {
            int t=ans2;

            ans2+=min(rate, d[i-1]);

            //cout<<"-- "<<ans2-t<<endl;
        }
        cout<<"Case #"<<cas<<": "<<ans1<<" "<<ans2<<endl;
    }

    return 0;
}
