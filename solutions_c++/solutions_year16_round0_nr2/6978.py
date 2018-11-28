#include<bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define ll long long int
#define MOD 1000000007

using namespace std; 

int A[10];

string S;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,n,ans;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		ans=0;
		cin>>S;
		n=S.length();
		while(n&&S[n-1]=='+')
			n--;
		if(n<=0)
		{
			printf("Case #%d: %d\n",k,0);
			continue;
		}
		int i=0;
		if(S[i]=='+')
		{
			while(i<n&&S[i]=='+')
				i++;
			ans=1;
		}
		for(;i<n;i++)
		{
			while(i<n&&S[i]=='-')
				i++;
			if(i>=n)
				break;
			while(i<n&&S[i]=='+')
				i++;
			i--;
			ans+=2;
		}			
		printf("Case #%d: %d\n",k,ans+1);
	}
	return 0;
}
