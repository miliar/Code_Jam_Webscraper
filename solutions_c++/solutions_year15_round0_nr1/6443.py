#include <bits/stdc++.h>

using namespace std;

int main(int argc, char** argv) {
	freopen("inA.txt","r",stdin);
	freopen("outA.txt","w",stdout);
	string s;
	long long cases,invited,pc,n=1,s_max;
	cin>>cases;
	while(cases--)
	{
		cin>>s_max;
		cin>>s;
		invited=0;
		pc=s[0]-'0';
		for(int i=1;i<s.size();i++)
		{
			if(s[i]=='0')
			continue;
			
			if(pc<i)
			{
				invited += i-pc;
				pc += i-pc;
			}
			pc+=s[i]-'0';
		}
		cout<<"Case #"<<n++<<": "<<invited<<endl;
	}
	return 0;
}

