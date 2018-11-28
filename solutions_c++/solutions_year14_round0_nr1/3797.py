#define _CRT_SECURE_NO_WARNINGS
#include<bits/stdc++.h>
using namespace std;
main()
{
    freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	register int i,j,t,m=1,k,l,n;
	int ans1,ans2,a[4][4],b[4][4];
	cin>>t;
	while(t--)
    {
        register int c=0;
        cin>>ans1;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            cin>>a[i][j];
        }

    }
    cin>>ans2;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            cin>>b[i][j];
        }

    }
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
        if(a[(ans1-1)][i] == b[(ans2-1)][j])
            {
                c++;
                k=a[(ans1-1)][i];

        }
    }
    }
    cout<<"Case #"<<m++<<": " ;
    if(c==1)
    cout<<k<<endl;
    else if(c==0)
        cout<<"Volunteer cheated!"<<endl;
    else if(c!=0 || c!=1)
         cout<<"Bad magician!"<<endl;

    }
    }
