#include<bits/stdc++.h>

using namespace std;

int calculate(char S[])
{
	int ans=0;
	int end = strlen(S) - 1;
	
	while(end>=0 && S[end]!='-')
		end--;

	S[end+1] = '\0';
	
	while(end>=0)
	{
		int i = 0;
		for(i=0; S[i] && S[i]!='-';i++)
			S[i] = '-';
			
		if(i)	
			ans++;
		
		reverse(S,S+(end+1));
		
		for(i=0; S[i];i++)
			S[i] = (S[i] == '-')?'+':'-';
			
		while(end>=0 && S[end]!='-')
			end--;
		S[end+1] = '\0';
		
		ans++;
	}
	
	return ans;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int T;
	
	cin>>T;
	
	for(int t=1;t<=T;t++)
	{
		char S[105];
		
		cin>>S;
		
		int ans = 0;
		
		ans = calculate(S);
		
		cout<<"Case #"<<t<<": "<<ans<<'\n';
	}
	
	return 0;
}
