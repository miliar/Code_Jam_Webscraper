#include <bits/stdc++.h>
using namespace std;
int main() 
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tes,k,c,s;
    cin>>tes;
    int q=0;
    while(tes--)
    {
        cout<<"Case #" <<++q<<": ";
        cin>>k>>c>>s;
        for(int i=1;i<=k;i++)cout<<i<<" ";
            cout<<"\n";
    }   
    return 0;
}
