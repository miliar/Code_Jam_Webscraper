#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        long long n;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<t<<": ";
            cout<<"INSOMNIA\n";
            continue;
        }
        set<int> s;
        long long i=1;
        long long no=n;
        long long ans=0;
        while(s.size()<10)
        {
            no=i*n;
            long long temp=no;
            while(temp)
            {
                int z=temp%10;
                s.insert(z);
                temp=temp/10;
                if(s.size()==10)
                {
                    ans=no;
                    break;
                }
            }
            i++;
        }
        cout<<"Case #"<<t<<": ";
        cout<<ans<<endl;
    }
    return 0;
}
