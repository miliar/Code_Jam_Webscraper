#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	ll t,k,c,s,i;
	cin>>t;
	FILE * pFile;
	pFile = fopen ("output.txt","w");
	ll cc=0;
	while(t--)
	{
		cc+=1;
		cin>>k>>c>>s;
		ll aa=c;
		fprintf (pFile, "Case #%lld: ",cc);
		for(i=1;i<=s;i++)
		{
			fprintf (pFile, "%lld ",i);
			//aa*=s;
		}
		fprintf (pFile, "\n");
	}
}
