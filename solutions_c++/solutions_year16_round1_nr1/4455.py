#include <iostream>
#include<string>
using namespace std;

int main() {
	// your code goes here
	int tr;
	cin>>tr;
	int r=1;
	while(r<=tr)
	{
		string sa;
		cin>>sa;
		int n=sa.length();
		string res; res=sa[0];
		for(int i=1;i<n;i++)
		{
			if(res[0]<=sa[i])
			res=sa[i]+res;
			else
			res=res+sa[i];
		}
		cout<<"Case #"<<r<<": "<<res<<"\n";
		r++;
	}
	return 0;
}