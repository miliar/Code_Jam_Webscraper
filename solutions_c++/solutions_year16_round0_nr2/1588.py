#include<iostream>
using namespace std;
string s;
int main()
{
	int t , coun = 0 ,ans;
	cin>>t;
	while(t--)
	{
		coun++;
		cin>>s;
		int l = s.length();
		ans = 0; 
		for(int i =0;i<l-1;i++)
		{
			if(s[i] !=s[i+1])
			ans++;
		}
		if(s[l-1] == '-')
		ans++;
		cout<<"Case #"<<coun<<": "<<ans<<endl;
	}
}
