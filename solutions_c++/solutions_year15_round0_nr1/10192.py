#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t, j=1;
	cin>>t;
	while(t--)
	{
		int l, n, i, f=0, p=0;
		string s;
		cin>>l>>s;
		p=s[0]-'0';
		for(i=1; i<=l; i++)
		{
			n=s[i]-'0';
			if(p<i&&n!=0)
			{
				f+=i-p;p+=f;
			}
		//	cout<<f<<endl;
			p+=n;
		}
		cout<<"Case #"<<j++<<": "<<f<<endl;
	}
	return 0;
}