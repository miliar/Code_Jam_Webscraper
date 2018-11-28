#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int coun = 0;
    while(t--)
    {
        coun++;
        string s;
        cin>>s;
        int n = s.length();
        string ans = "";
        for(int i = 0;i< n;i++)
        {
            if(s[i] >= ans[0])
                ans = s[i]+ans;
            else
                ans = ans+s[i];
        }
        cout<<"Case #"<<coun<<": "<<ans<<endl;
    }

}
