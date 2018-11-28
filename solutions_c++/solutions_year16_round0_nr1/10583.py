#include<iostream>
using namespace std;
int main()
{
    long long int t;
    cin >> t;
    long long int u;
    for(u=1;u<=t;u++)
    {
        long long int n;
        cin >> n;
        long long int a[10];
        long long int i;
        for(i=0;i<10;i++)
        {
            a[i]=0;
        }
        long long int c=0;
        long long int t;
        if(n==0)
        {
            cout << "Case #"<<u<<": INSOMNIA\n";
        }
        long long int ans;
        while(n!=0)
        {
            long long int is=0;
            for(i=0;i<10;i++)
            {
                if(a[i]==0)
                is=1;
            }
            if(is==0)
            {
                cout << "Case #"<<u<<": "<<ans<<"\n";
                break;
            }
            
            c=c+1;
            t=c*n;
            ans=t;
            while(t)
            {
                int d;
                d=t%10;
                a[d]++;
                t=t/10;
            }
            
        }
    }
}