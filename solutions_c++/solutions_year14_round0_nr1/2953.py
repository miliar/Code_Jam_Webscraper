#include<iostream>
#include<stdio.h>
#define forn(i,n) for(i=0;i<n;i++)

using namespace std;
int main()
{
	int t;
	freopen("prob1_small.in","r",stdin);
	freopen("prob1_small.txt","w",stdout);
	cin>>t;
	for(int p=1;p<=t;p++)
	{
        int a[4][4],b[4][4],a1,a2,i,j;
        cin>>a1;
        forn(i,4) forn(j,4) cin>>a[i][j];
        cin>>a2;
        forn(i,4) forn(j,4) cin>>b[i][j];

        int counter=0,val;
        forn(i,4)
            forn(j,4)
                if(a[a1-1][i]==b[a2-1][j])
                {
                    counter++;
                    val=a[a1-1][i];
                }

        cout<<"Case #"<<p<<": ";

        if(counter==1) cout<<val;
        else if(counter>1) cout<<"Bad magician!";
        else cout<<"Volunteer cheated!";

		cout<<endl;
	}
    return 0;
}
