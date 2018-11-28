#include<stdio.h>
#include<iostream>
#include<set>
using namespace std;
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin>>t;
    for(int i=1 ; i<=t ; i++)
    {
        long long int n, b, r;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        }
        else
        {
            r=n;
        set<int> sts;
        b=n;
        while(b)
        {
                sts.insert(b%10);
                b/=10;
        }

        while(sts.size()!=10)
        {
            n+=r;
            b=n;
            while(b)
            {
                sts.insert(b%10);
                b/=10;
            }

        }
        cout<<"Case #"<<i<<": "<<n<<endl;
        }
    }
}
