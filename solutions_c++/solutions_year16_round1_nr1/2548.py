#include<bits/stdc++.h>
#define ll long long
#define endl '\n'
#define max 1000000
using namespace std;
string s,ans;

int main()
{
	ios_base::sync_with_stdio(false);
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w+",stdout);
	int coun=1,t;
	cin>>t;
	int k=20,j=20;
	while(coun<=t)
	{
		j=20;
		k=20;
		cin>>s;
		ans[j]=s[0];
		for(int i=1;i<s.size();i++)
		{
			if((s[i]-48)>=(ans[k]-48))
			{
				k--;
				ans[k]=s[i];
				
			}
			else
			{
				j++;
				ans[j]=s[i];
			}
		}
			cout<<"Case #"<<coun<<": ";
		ans[j+1]='\0';
		while(ans[k]!='\0')
		{
			cout<<ans[k];
			k++;
		}
		cout<<endl;
		coun++;
	}
	
}
