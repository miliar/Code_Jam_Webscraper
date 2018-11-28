#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long n,k,c,s,j,i;
    freopen("TasnimIN.txt","r",stdin);
    freopen("TasnimOUT.txt","w",stdout);
    cin>> n;
    for(j=1;j<=n;j++)
    {
        cin>>k >> c >> s;
        cout << "Case #" << j << ": ";
        if(k!=s)
            cout << "IMPOSSIBLE" ;
        else{
        for(i=1;i<=s;i++)
            cout << i  << " " ;
        }
        cout << endl;
    }
}
