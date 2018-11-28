
#include<bits/stdc++.h>
typedef long long ll;
using namespace std;


int main()
{
	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		
		string s;
		cin>>s;
		string sc=s;
	//	sort(s.begin(), s.end());
		int l=s.length();
		int count[26];
		
		for(int i=0;i<26;i++)
		count[i]=0;
		
		for(int i=0;i<l;i++)
		{
			count[s[i]-'A']++;
			
		}
		
		int count7=count['V'-'A']-(count['F'-'A']-count['U'-'A']);
		int count5=(count['F'-'A']-count['U'-'A']);
		int count1=(count['O'-'A'])-(count['Z'-'A']+count['W'-'A']+count['U'-'A']);
		int count9=0.5*((count['N'-'A'])-(count1+count7));
		int count3=count['R'-'A']-(count['Z'-'A']+count['U'-'A']);
		
		int fc[10]={count['Z'-'A'],count1,count['W'-'A'],count3,count['U'-'A'],count5,count['X'-'A'],count7,count['G'-'A'],count9};
		
		cout<<"Case #"<<(i+1)<<": ";
		for(int i=0;i<=9;i++)
		{
			while(fc[i]--)
			cout<<i;
		}
		cout<<endl;
	}
	
	return 0;
}
	

