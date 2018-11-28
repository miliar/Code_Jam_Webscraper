#include<bits/stdc++.h>
using namespace std;
int main()
{
     freopen("A-large.in", "r", stdin);
freopen("output.txt", "w", stdout);
    long long int test;
    cin>>test;
    for(int i=1;i<=test;i++)
    {
        long long int n;
        cin>>n;
        if(n==0)
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else{
            long long res,ans;
            set<int>s;
            for(int i=1;i<2000;i++)
            {
                res=i*n;
                ans=i*n;
                while(res!=0)
                {
                    s.insert(res%10);
                    res=res/10;
                }
                if(s.size()==10)
                    break;
            }
             cout<<"Case #"<<i<<": "<<ans<<endl;
        }

    }
    return 0;
}
