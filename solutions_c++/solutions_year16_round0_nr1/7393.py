#include<iostream>
using namespace std;
int main()
{
    long long int t, N;
    cin>>t;
    int x;
    for(int i=1; i<=t; i++)
    {
        cin>>N;
        int c=10;
        if(N==0) cout<<"\nCase #"<<i<<": ÏNSOMNIA\n";
        else
        {
            int a[10]={0};
            for(int j=1; ;j++)
            {
                x=N*j;
                int p=x;
                while(p)
                {
                    if(a[p%10]==0)
                    {
                        a[p%10]=1;
                        c--;
                    }
                    p/=10;
                }
                if(c==0) break;
            }
            cout<<"Case #"<<i<<": "<<x<<"\n";
        }
    }
    return 0;
}
