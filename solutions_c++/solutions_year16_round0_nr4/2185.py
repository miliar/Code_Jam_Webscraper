#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<queue>
#include<algorithm>
#include<stack>
using namespace std;
long long t,k,c,s;
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    ofstream cout;
    cout.open("D-small-attempt0.out");
    scanf("%lld",&t);
    for(int o=1; o<=t; o++)
    {
        scanf("%lld%lld%lld",&k,&c,&s);
        cout<<"Case #"<<o<<":";
        long long p=1;
        c-=2;
        while(c>=0) {p*=k; c--;}
        for(long long i=1; i<=p*k; i+=p)
        {
            cout<<" "<<i;
        }
        cout<<endl;
    }
    cout.close();
    return 0;
}
