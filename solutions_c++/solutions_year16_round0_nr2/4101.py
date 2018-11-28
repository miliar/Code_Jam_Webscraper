#include <bits/stdc++.h>
using namespace std;
int main() 
{
	ifstream input;
    ofstream output;
    input.open("B-large.in");
    output.open("output.txt");
	int t,j=1;
	input>>t;
	while(t--)
	{
		string s;
		int i,cnt=0,ans;
		input>>s;
		for(i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				while(s[i]=='-')
				i++;
				cnt++;
			}
		}
		if(s[0]=='+')
		ans=2*cnt;
		else
		ans=2*cnt-1;
		output<<"Case #"<<j<<":";
		j++;
		output<<" "<<ans<<endl;
	}
	output.close();
	input.close();
	//sakshamsinghnsit
	return 0;
}
