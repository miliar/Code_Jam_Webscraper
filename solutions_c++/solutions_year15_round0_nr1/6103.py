#include<bits/stdc++.h>

using namespace std;

int main(void)
{
    freopen("A-large.in", "r", stdin);
    freopen("res_large.out", "w", stdout);
    int t;
    cin>>t;
    int k = t;
    while(t--)
    {
        int n;
        cin>>n;
        n++;
        string inp;
        cin>>inp;
        //cout<<n-1<<" "<<inp<<"\n";
        int a[n];
        a[0] = 0;
        int res = 0;
        for(int i=1; i<n; i++)
        {
            long long int tmp = a[i-1] + inp[i-1] - 48;
            if(tmp >= i)
                a[i] = tmp;
            else
            {
                res += i-tmp;
                a[i] = i;
            }
        }
        cout<<"Case #"<<k-t<<": "<<res<<endl;
    }
    return 0;
}
