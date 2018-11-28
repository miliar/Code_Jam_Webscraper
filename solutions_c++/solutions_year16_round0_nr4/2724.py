#include <iostream>
using namespace std;

int main()
{
    int t, k, c, s;
    cin>>t;
    for(int i = 1; i <= t; i++)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<i<<": ";
        if(c == 1 || k == 1)
            cout<<1<<" ";
        for(int j = 2; j <= k; j++)
            cout<<j<<" ";
        cout<<"\n";
    }

    return 0;
}
