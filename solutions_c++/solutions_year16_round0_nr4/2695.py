#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;
int main()
{
    LL t,k,c,s,cnt=0,i;
     FILE *fin = freopen("D-small.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("D-small.out", "w", stdout);
    cin>>t;
    cnt=1;
    while(t--)
    {
        cin>>k>>c>>s;

        cout<<"Case #"<<cnt<<": ";

        for(i=1;i<=k;i++)
        {
            cout<<i<<" ";
        }
        cout<<"\n";
        cnt++;
    }
    return 0;
}
