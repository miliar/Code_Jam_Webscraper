#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,cs=1,k,c,s;
    cin>>t;
    string ss;
    while(t--)
    {
        cin>>k>>c>>s;
        printf("Case #%d: 1", cs++);
        for(int i = 2; i <= s; i++) cout<<" "<<i;
        cout<<"\n";
    }
    return 0;
}
