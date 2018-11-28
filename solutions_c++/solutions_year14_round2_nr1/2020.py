#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main()
{
	bool fegla=false;
	int t, n, i, j, k, l, a0, a1, ans;
	string s[3];
	cin>>t;
	for(i=1; i<=t; i++)
	{
		cin>>n;
		for(j=0; j<n; j++) cin>>s[j];
		ans=0; 
		j=0; 
		k=0;
		fegla=false;
		while(j<s[0].length() || k<s[1].length())
		{
			if(s[0][j]==s[1][k])
			{
				a0=1; a1=1;

				l=j+1;
				while(s[0][l]==s[0][j])
				{
					a0++;
					l++;
				}
				j=l;

				l=k+1;
				while(s[1][l]==s[1][k])
				{
					a1++;
					l++;
				}
				k=l;
				
				ans+=abs((a1-a0));
			}
			else
			{
				fegla=true;
				break;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(fegla==true) cout<<"Fegla Won"<<endl;
		else cout<<ans<<endl;
	}

	return 0;
}
