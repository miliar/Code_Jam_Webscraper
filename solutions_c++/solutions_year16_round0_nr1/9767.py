#include<iostream>
using namespace std;
int main()
{
    long long int T, n;
    cin>>T;
    int y;
    for(int i=1; i<=t; i++)
    {
        cin>>n;
        int c=10;
        if(n==0) cout<<"\nCase #"<<i<<": ÏNSOMNIA\n";
        else
        {
            int a[10]={0};
            for(int j=1; ;j++)
            {
                y=n*j;
                int p=y;
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
            cout<<"Case #"<<i<<": "<<y<<"\n";
        }
    }
    return 0;
}
