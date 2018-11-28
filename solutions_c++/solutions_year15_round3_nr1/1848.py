//om namah shivaya
#include<bits/stdc++.h>
using namespace std;
typedef long long unsigned llu;

int main()
{
    int t;
    cin >> t;
    for(int tt=0;tt<t;tt++)
    {
        int r,c,w;
        cin>>r>>c>>w;
        cout << "Case #" << (tt+1) << ": ";
        double v=(double)c/w;
        if(ceil(v)==floor(v))
            cout<<v+w-1<<endl;
        else
        {cout<<(int)v+w<<endl;}
    }
    return 0;
}
