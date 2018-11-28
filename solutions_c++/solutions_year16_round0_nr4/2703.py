#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long int t,m,k,c,s,cnt=0,j;
     FILE *fin = freopen("E-small.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("E-small.out", "w", stdout);
    cin>>t;
    cnt=1;
    while(t--)
    {
        cin>>m>>c>>k;

        cout<<"Case #"<<cnt<<": ";

        for(j=1;j<=m;j++)
        {
            cout<<j<<" ";
        }
        cout<<"\n";
        cnt++;
    }
    return 0;
}
