#include <bits/stdc++.h>
using namespace std;

int ans=0;
void func(string s)
{
	if(s.length()==0)
		return ;
	else if(s[s.length()-1]=='+'){
		func(s.substr(0,s.length()-1));
	}
	else if(s[s.length()-1]=='-'){
		if(s[0]=='+')
		{
			s[0]='-';
			int i=1;
			while(s[i]!='-')
			{
				s[i]='-';
				i++;
			}
			ans++;
		}
		int k=s.length()-1;
		int i=0;
		string cp=s;
		for(i=0;i<=k;i++){
			s[i]=(cp[k-i]=='+')?'-':'+';
		}
		//cout << "oye jhantu: " << s << endl;
		ans++;
		func(s.substr(0,s.length()-1));
	}

		


}
int main()
{
	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		ans=0;
		string s;
		cin >> s;
		string cp=s;
		int j=1;
		for(int i=1;i<s.length();i++){
			if(s[i]==s[i-1]){
				cp.erase(j,1);
			}
			else
				j++;
		}
		func(cp);
		cout <<"Case #" << t << ": " << ans << endl;
	}	

}
