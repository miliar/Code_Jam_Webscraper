#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int a,b,k;
    for(int i=1;i<=t;i++)
    {
        long long wynik=0;
        cin>>a>>b>>k;
        if(a<b) swap(a,b);
        for(int c=0;c<b;c++)
        {
            for(int d=0;d<a;d++)
            {
                //cout<<d<<" "<<c<<" "<<(d&c)<<endl;
                if((d&c)<k) wynik++;
            }
        }
        cout<<"Case #"<<i<<": "<<wynik<<endl;
    }
}
