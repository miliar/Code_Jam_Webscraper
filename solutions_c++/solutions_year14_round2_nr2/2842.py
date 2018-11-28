//CODER:   AmanSharma
//CONTEST: ROUND 1 (B) CODE JAM  2014

#include<iostream>
#include<stdio.h>
#include<math.h>
#define forn(i,n) for(i=0;i<n;i++)
#define maxi(a,b) ((a > b) ? a : b)
#define mini(a,b) ((a > b) ? b : a)

using namespace std;
int main()
{
	int t;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("A_res.txt","w",stdout);
	cin>>t;
	for(int p=1;p<=t;p++)
	{
        long long a,i,j,b,k,count=0;
        cin>>a>>b>>k;
        forn(i,a)
            forn(j,b)
            {
                //cout<<i<<" "<<j<<" : "<<(i&j)<<endl;
                if((i&j)<k)
                    count++;

            }

        cout<<"Case #"<<p<<": "<<count;
        cout<<endl;
	}
    return 0;
}
