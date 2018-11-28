#include <bits/stdc++.h>
using namespace std;
int main() {
    freopen("A-large.in","r",stdin);
    freopen("ak1.out","w",stdout);
	long long int t,j;
	cin>>t;
	for(j=1;j<=t;j++)
	{
	    long long int i,n,ct=0,z=0;
	    char s[2000];
	    cin>>n;
	    cin>>s;
	    for(i=0;i<=n;i++)
	    {
	        if(ct<i)
	        {
	            z+=i-ct;
                ct+=i-ct;
            }
            ct+=(s[i]-48);
	    }
	    cout<<"Case #"<<j<<": "<<z<<endl;
	}
	return 0;
}
