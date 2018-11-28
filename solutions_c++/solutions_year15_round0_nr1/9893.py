#include<bits/stdc++.h>
#define INF 100000
using namespace std;



int main()
{
    std::ios::sync_with_stdio(false);
    cin.tie(0);


    int t,n;
    cin>>t;
    n=t;
    while(t--)
    {
        int Smax;
        cin>>Smax;
        string S;
        cin>>S;
        int a[Smax+1];
        for(int i=0;i<=Smax;i++)
        {
            a[i]=S[i]-'0';
        }
        long long total=a[0];
        int count=0;
        for(int i=1;i<=Smax;i++)
        {
            if(a[i]==0)
                continue;
            if(total<i)
            {
                count+=i-total;
                total+=a[i]+count;
            }
            else
                total+=a[i];
        }
        cout<<"Case #"<<n-t<<": "<<count<<endl;
    }


    return 0;
}

