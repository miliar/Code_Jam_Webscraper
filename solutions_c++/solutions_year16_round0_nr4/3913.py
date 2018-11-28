#include <iostream>

using namespace std;

int main()
{
    int t,s,k,c,j,i;
    cin>>t;
    j=1;
    while(t--)
    {
        cin>>k>>c>>s;
        if((s<k-1)||(c==1 && s<k))
            cout<<"Case #"<<j<<": IMPOSSIBLE\n";
        else if(c==1 && s>=k)
            {cout<<"Case #"<<j<<": ";
            for(i=1;i<=k;i++)
            cout<<i<<" ";
        cout<<"\n";}
        else
        {
            cout<<"Case #"<<j<<": ";
            if(k!=1)
            {
            for(i=2;i<=k;i++)
            cout<<i<<" ";
        cout<<"\n";
            }
            else cout<<"1\n";

        }
j++;
    }
    return 0;
}
