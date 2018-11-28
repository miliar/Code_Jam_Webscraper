#include<bits/stdc++.h>
using namespace std;

#define f(i, a, b) for(int i=a; i<=b; i++)

int main()
{
    int T, k, c, s;
    unsigned long long pot = 1;


    cin>>T;

    f(t, 1, T)
    {
        cin>>k>>c>>s;

        pot=1;
        f(i, 1, c-1)
            pot*=k;
        cout<<"Case #"<<t<<": ";
        f(i, 0, k-1)
            cout<<1+i*pot<<" ";
        cout<<endl;
    }




    return 0;
}
