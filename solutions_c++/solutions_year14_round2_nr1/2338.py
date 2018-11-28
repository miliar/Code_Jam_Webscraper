#include<iostream>
#include<string>
#include<vector>

int abs(int a)
{
	if(a>0) return a;
	else return (a*(-1));
}

using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		cout<<"Case #"<<tc<<": ";
		bool found = true;
		int n;
		cin>>n;
		string a,b;
		cin>>a>>b;
		int ans = 0;
		int i=0,j=0;
		while( i<a.length() || j<b.length() )
		{
			int k=i,l=j;
			while(a[i]==a[k]) k++;
			k--;
			while(b[j]==b[l]) l++;
			l--;
			if(a[k]!=b[l])
			{
				found = false;
				cout<<"Fegla Won\n";
				break;
			}
			ans += abs( (k-i) - (l-j) );
			i=k+1;
			j=l+1;
		}
		if(found) cout<<ans<<"\n";
	}
	
	return 0;
}
