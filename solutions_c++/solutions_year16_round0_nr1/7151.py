#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, n, ans;
    cin>>T;
    for(int t=1; t<=T; t++)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<t<<": INSOMNIA"<<endl;
        }
        else
        {
            set<int>st;
            int cnt = 1;
            int temp;
            while(st.size()!=10)
            {
                temp = n*cnt++;
                ans = temp;
                while(temp!=0)
                {
                    st.insert(temp%10);
                    temp/=10;
                }
            }
            cout<<"Case #"<<t<<": "<<ans<<endl;
        }
    }
}
