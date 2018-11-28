#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output1.txt", "w", stdout);
    int t,cases,a[100005];
    cin>>t;
    cases = 0;
    while(t--)
    {
        cases++;
        int n;
        cin>>n;
        for(int i = 0; i < n; i++)
        {
            cin>>a[i];
        }
        sort(a, a+ n);
        reverse(a, a+n);
        long long int mn = INT_MAX;
        for(int i = 1; i <= 10005; i++)
        {
            long long  ans = i;
            for(int j = 0; j < n; j++)
            {
                int k = ((a[j] - i)/i);
                if( i <  a[j]) {
                    if( (a[j] - i)%i == 0 ) {
                            ans = ans+ k;
                    } else {
                            ans = ans + k + 1;
                    }
                }
            }
            if( ans < mn)
            {
                mn = ans ;
            }
            //cout<<endl;
        }

        cout<<"Case #"<<cases<<": "<<mn <<endl;
    }

    return 0;
}

