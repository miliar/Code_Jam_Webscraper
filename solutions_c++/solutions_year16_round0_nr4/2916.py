#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int K,C,S,T;

int main()
{
    freopen("D-small-attempt0.in.txt","r",stdin);
    freopen("A-large.out.txt","w",stdout);
    cin>>T;
    for(int k=1;k<=T;k++)
    {
        cin>>K>>C>>S;
        cout<<"Case #"<<k<<":";
        long long int t=1;
        for(int i=1;i<C;i++)
            t*=K;
        for(long long i=1,j=0;j<S;j++,i+=t)
            cout<<" "<<i;
        cout<<endl;
    }
    return 0;
}
