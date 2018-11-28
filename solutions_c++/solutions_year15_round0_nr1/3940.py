/********************************/
/***  Coded By Ankush Sharma  ***/
/********************************/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    //std::ios::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, c; cin>>t;
    c=t;
    while(t--)
    {
        int s; cin>>s;
        char arr[s+1];
        for(int i=0; i<=s; i++)
            cin>>arr[i];

        int req=0, cur=arr[0]-'0';
        for(int i=1; i<=s; i++)
        {
            if(cur<i)
            {
                int add=i-cur;
                req+=add;
                cur+=add;
            }
            cur+=arr[i]-'0';
        }
        cout<<"Case #"<<c-t<<": " <<req<<"\n";
    }
    return 0;
}

