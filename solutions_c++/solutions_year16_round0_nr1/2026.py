#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tn;
    cin>>tn;
    for(int tc=1; tc<=tn; tc++)
    {
        bool used[10];
        for(int i=0; i<10; i++)
            used[i]=0;
        int c = 0;
        int n;
        cin>>n;
        long long ans = 0;
        if(n!=0)
            for(long long i=n; true; i+=n)
            {
                long long t = i;
                while(t)
                {
                    if(!used[t%10])
                    {
                        c++;
                        used[t%10]=true;
                    }
                    t/=10;
                }
                if(c==10)
                {
                    ans=i;
                    break;
                }
            }
        cout<<"Case #"<<tc<<": ";
        if(ans)
            cout<<ans<<endl;
        else
            cout<<"INSOMNIA"<<endl;
    }
    return 0;
}