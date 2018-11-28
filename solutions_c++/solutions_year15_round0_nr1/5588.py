#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    int T;
    cin>>T;
    int q = 1;
    while(q<=T)
    {
        int l;
        string x;
        cin>>l>>x;
        int ans = 0;
        int till = 0;
        for(int i=0;i<=l;i++)
        {
            char curr = x[i];
            int cur = int(curr)-48;
            if(till >= i)
            {
                till += cur;
            }
            else
            {
                ans += i-till;
                till = i + cur;
            }
        }
        cout<<"Case #"<<q<<": "<<ans<<endl;
        q = q+1;
    }
}
