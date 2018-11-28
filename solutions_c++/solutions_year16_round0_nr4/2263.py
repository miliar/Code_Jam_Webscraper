#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int k,c,s;
    int T,Case=1;
    cin>>T;
    while(T--)
    {
        printf("Case #%d:",Case++);
        cin>>k>>c>>s;
        for(int i=1;i<=k;i++)
        {
            cout<<" "<<i;
        }
        cout<<endl;
    } 
    return 0;
}
