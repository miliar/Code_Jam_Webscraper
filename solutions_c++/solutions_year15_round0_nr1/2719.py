#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    freopen("A-large.in", "r",stdin);
    freopen("a.out","w",stdout);

    int T;
    cin>>T;
    for (int cas=1; cas<=T; cas++)
    {
        int n;
        string s;
        cin>>n>>s;
        int ans=0;
        int sum=s[0]-'0';
        int len = s.size();
        while (len>0 && s[len-1]=='0') len--;
        for (int i=1; i<len; i++)
        {
            if (sum<i)
            {
                ans+=i-sum;
                sum=i;
            }
            sum+=s[i]-'0';
        }

        cout<<"Case #"<<cas<<": "<<ans<<endl;
    }
    return 0;
}
