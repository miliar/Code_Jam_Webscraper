#include <bits/stdc++.h>

using namespace std;

bool check(string s)
{
	bool chars[26];
	for (int i = 0; i < 26; ++i)
	{
		chars[i]=false;
	}
	int ind=0;
	bool poss=true;
	while(ind<s.length() && poss)
	{
		if(chars[s[ind]-'a']==true){
			poss=false;
		}
		else
		{
			chars[s[ind]-'a']=true;
			int temp=ind;
			while(ind<s.length() && s[temp] == s[ind])
			{
				ind++;
			}
			//if(ind!=temp+1)ind--;
		}
	}
	return poss;
}

int main()
{
	int t;
	cin>>t;
	for (int i = 0; i < t; ++i)
	{
		int n;
		cin>>n;
		string arr[n];	int t_arr[n];
		for (int j = 0; j < n; ++j)
		{
			cin>>arr[j];
			t_arr[j]=j;
		}
		long long int ans=0;
		do
		{
			string test="";
			for (int j = 0; j < n; ++j)
			{
				test+=arr[t_arr[j]];
			}
			if(check(test))ans++;
		}
		while(next_permutation(t_arr,t_arr+n));
		//stuff ,ans 
		cout<<"Case #"<<(i+1)<<": "<<(ans%1000000007)<<endl;
	}
	return 0;
}