#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	int cases=1;
	while(t--)
	{
		int n;
		cin>>n;
		string s;
		cin>>s;
		int ans=0;
		int count=0;
		for(int i=0;i<s.length();i++)
		{
			if(i>count&&(s[i]-'0')!=0)
			{
				ans+=(i-count);
				count+=(i-count);
			}
			count+=(s[i]-'0');
		}
		cout<<"Case #"<<cases<<": "<<ans<<endl;
		cases++;
	}
	return 0;
}
