#include <bits/stdc++.h>
#define mod 1000000009
using namespace std;

long long int powr (long long int a, long long int b)
{
    if (b == 0)
        return 1;
    long long int x = powr(a, b/2);
    if (b % 2 == 0)
        return (x*x)%mod;
    else
        return (((x*x)%mod)*a)%mod;
}

int main() {
	// your code goes here
	ios_base::sync_with_stdio(false);
	cin.tie(0),cout.tie(0);
	int t,i,j,k,c,s;
	string st;
	cin>>t;
	j=1;
	while(t--)
	{
	    cin>>k>>c>>s;
	    cout<<"Case #"<<j<<":";
	    for(i=1;i<=k;i++)
	    cout<<" "<<i;
	    cout<<"\n";
	    j++;
	}
	return 0;
}
