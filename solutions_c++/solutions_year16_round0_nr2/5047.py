#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long 
#define ll long long
#define MAX 100
#define pb push_back
#define gc getchar
#define mp make_pair
#define fast(){cin.sync_with_stdio(0);cin.tie(0);cout.tie(0);}
int main()
{
	//freopen("B-large.in","r+",stdin);
	//freopen("output2large.txt","w+",stdout);
	int t;
	cin>>t;
	int cases=0;
	while(t--)
	{
		cases++;
		string s;
		cin>>s;
		int n=s.length();
		bool f=1;
		int ans=0;
		cout<<"Case #"<<cases<<": ";
		if(n==1)
			if(s[0]=='-')cout<<1<<"\n";
			else cout<<0<<"\n";
		else
		{
			int ans=0;
			while(f)
			{
				int i;
				for(i=1;i<n;i++)
				{
					if(s[i]!=s[i-1])
					 break;
				}
				if(i==n)
				{
					if(s[i-1]=='+')
					 {f=0;break;}
					else
					 {ans++;f=0;break;}
				}
				else
				{
					for(int j=0;j<i;j++)
					{
						s[j]=s[i];
					}
					ans++;
				}
				
			}
			cout<<ans<<"\n";
		}
		
	}
	
}
