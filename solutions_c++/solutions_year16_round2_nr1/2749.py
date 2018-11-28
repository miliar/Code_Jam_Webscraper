#include "bits/stdc++.h"
using namespace std;
int ord(char a)
{
	return a - 'A';
}
bool check(int arr[], string s)
{
	int b[26];
	for (int i = 0; i < 26; ++i)
		b[i] =arr[i];

	for (int i = 0; i < s.length(); ++i)
	{
		if(b[s[i] - 'A'] <= 0)
			return false;
		else
			b[s[i] - 'A']--;
	}

	for (int i = 0; i < s.length(); ++i)
		arr[s[i] - 'A']--;
	//cout<<s<<" "<<arr[19]<<endl;
	return true;
}
int main()
{
	int t;
	string s;
	cin>>t;
	for (int i = 1; i <=t; ++i)
	{
		cin>>s;
		string ans;
		int arr[26];
		for(int j=0; j<26; j++)
			arr[j] = 0;
		for(int j=0; j<s.length(); j++)
			arr[s[j] - 'A']++;
		
		bool t  = true;
		if(arr[ord('X')] > 0)
		{
			t  = true;
			while(t)
			{
				t = check(arr, "SIX");
				if(t)
					ans += "6";
			}
		}
		if(arr[ord('Z')] > 0)
		{
			t = true;
			while(t)
			{
				t = check(arr, "ZERO");
				if(t)
					ans += "0";
			}
		}
		if(arr[ord('G')] > 0)
		{

			t  = true;
			while(t)
			{
				t = check(arr, "EIGHT");
				if(t)
					ans += "8";
			}	
		}
		
		if(arr[ord('W')] > 0)
		{
			t  = true;
			while(t)
			{
				t = check(arr, "TWO");
				if(t)
					ans += "2";
			}
		}
		if(arr[ord('H')] > 0)
		{
			t  = true;
			while(t)
			{
				t = check(arr, "THREE");
				if(t)
					ans += "3";
			}
		}
		if(arr[ord('U')] > 0)
		{
			t  = true;
			while(t)
			{
				t = check(arr, "FOUR");
				if(t)
					ans += "4";
			}
		}
		if(arr[ord('F')] > 0)
		{
			t  = true;
			while(t)
			{
				t = check(arr, "FIVE");
				if(t)
					ans += "5";
			}
		}
		if(arr[ord('V')] > 0)
		{
			t  = true;
			while(t)
			{
				t = check(arr, "SEVEN");
				if(t)
					ans += "7";
			}
		}
		if(arr[ord('O')] > 0)
		{
			t  = true;
			while(t)
			{
				t = check(arr, "ONE");
				if(t)
					ans += "1";
			}
		}
		if(arr[ord('N')] > 0)
		{
			t  = true;
			while(t)
			{
				t = check(arr, "NINE");
				if(t)
					ans += "9";
			}
		}

		sort(ans.begin(), ans.end());

		for(int j=0; j<26; j++)
		{
			if(arr[j]!=0)
			cout<<"L";
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}