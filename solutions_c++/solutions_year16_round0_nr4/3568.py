#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,k,c,s;
    long long int x,y;
    cin>>t;
    for(int j = 1; j <= t; j++)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<j<<": ";
        x = y = 1;
        for(int i = 1; i < c; i++)
        {
            x *= k;
        }
        for(int i = 1; i <= s; i++)
        {
            cout<<y<<" ";
            y += x;
        }
        cout<<endl;
    }
    return 0;
}
