#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-output0.out", "w", stdout);
    int cases, k, c, s;
    cin>>cases;

    for(int ca=1; ca<=cases; ca++)
    {
        printf("Case #%d: ", ca);
        cin>>k>>c>>s;
        for(int i=1; i<=s; i++)
            cout<<i<<" ";

        cout<<endl;
    }
    return 0;
}
