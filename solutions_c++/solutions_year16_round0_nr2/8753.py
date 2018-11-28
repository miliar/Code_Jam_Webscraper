#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

#define pb push_back
#define mp make_pair
#define f_inp ios_base::sync_with_stdio(false)
#define testcase ll test_case;cin>>test_case;while(test_case--)
#define lb lower_bound
#define ub upper_bound
#define F first
#define S second
#define mod 1000000007
#define lim 100005



int main()
{
    //f_inp;
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test_case;
    cin>>test_case;
    for(int h=1;h<=test_case;h++)
    {
        cout<<"Case #"<<h<<": ";
        string str;
        cin>>str;
        int ans  = 0;
        while(true)
        {
            bool ok = true;
            for(int i=0;i<str.length();i++)
            {
                if(str[i] == '-')
                    ok = false;
            }
            if(ok)
                break;
            ans++;
            if(str[0] == '+')
            {
                for(int i=0;i<str.length();i++)
                {
                    if(str[i] == '-')
                        break;
                    str[i] = '-';
                }
            }
            else
            {
                for(int i=0;i<str.length();i++)
                {
                    if(str[i] == '+')
                        break;
                    str[i] = '+';
                }
            }
        }
        cout<<ans<<"\n";
    }

    return 0;
}







