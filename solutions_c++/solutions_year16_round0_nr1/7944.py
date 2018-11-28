#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("a.txt", "w", stdout);
    long long t, cas, n, i, j, h[15], last, f, now, m;
    cin>>t;
    for(cas=1;cas<=t;cas++)
    {
        cin>>n;
        if(n==0)
            cout << "Case #" << cas <<": INSOMNIA\n";
        else
        {
            for(i=0;i<=9;i++)
                h[i] = 0;
            m=1;
            f=0;
            while(f==0)
            {
                now = n*m++;
                last = now;
                //cout << "  .. " << n << "\n";
                while(now>0)
                {
                    h[now%10] = 1;
                    now/=10;
                }
                int cnt = 0;
                for(i=0;i<=9;i++)
                {
                    if(h[i]==1)
                        cnt++;
                }
                if(cnt==10)
                {
                    f=1;
                    break;
                }
                if(m>1000000)
                    break;
            }
            if(f==1)
                cout << "Case #" << cas << ": " << last <<"\n";
            else
                 cout << "Case #" << cas <<": INSOMNIA\n";
        }
    }
    return 0;
}

