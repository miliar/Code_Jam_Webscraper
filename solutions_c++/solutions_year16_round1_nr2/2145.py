#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    FILE *fin = freopen("B-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B-large.out", "w", stdout);
    int n[100][50];
    int ha[2501];
    int t,no,h;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        memset(ha,0,sizeof(ha));
        cin>>no;
        for(int j=0;j<((2*no)-1);j++)
        {
            for(int k=0;k<no;k++)
            {
                cin>>n[j][k];
                h=n[j][k];
                ha[h]++;
            }
        }
        cout << "Case #" << i << ": ";
        for(int j=1;j<=2500;j++)
        {
            if((ha[j]%2)==1)
                cout<<j<<" ";
        }
        cout<<endl;
    }
    return 0;
}
