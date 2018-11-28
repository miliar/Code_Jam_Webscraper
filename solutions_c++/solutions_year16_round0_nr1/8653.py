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
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test_case;
    cin>>test_case;
    for(int h=1;h<=test_case;h++)
    {
        cout<<"Case #"<<h<<": ";
        int n;
        cin>>n;
        set<int> s;
        bool flag = false;
        for(int i=1;i<100000;i++)
        {
            ll x = (ll)n * (ll)i;
            ll temp = x;
            while(temp)
            {
                s.insert(temp%10);
                temp/=10;
            }
            if(s.size() == 10)
            {
                cout<<x<<"\n";
                flag = true;
                break;
            }
        }
        if(!flag)
        {
            cout<<"INSOMNIA\n";
        }
    }

    return 0;
}







