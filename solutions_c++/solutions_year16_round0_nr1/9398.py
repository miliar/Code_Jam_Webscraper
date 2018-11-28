#include <iostream>
#include <string>
#include <vector>

using namespace std;

int calc(int n)
{
    vector<bool> check(10, false);
    int cnt=0;

    int maxCheck=1000;
    for (int i=1; i<maxCheck; i++)
    {
        int t=n*i;
        int ret=t;
        //cout<<"MaxCheck "<<i<<" "<<t<<endl;
        while(t)
        {
            int d = t%10;
            if (!check[d])
            {
                //cout<<"d "<<d<<" cnt "<<cnt<<endl;
                check[d] = true;
                cnt++;
                if (cnt==10) return ret;
            }
            t/=10;
        }
        if (cnt==10) return ret;
    }

    return 0;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    cin>>T;
    for (int cas=1; cas<=T; cas++)
    {
        int n;
        cin>>n;
        if (n==0)
        {
            cout<<"Case #"<<cas<<": INSOMNIA"<<endl;
        }
        else
        {
            cout<<"Case #"<<cas<<": "<<calc(n)<<endl;
        }
    }

    return 0;
}
