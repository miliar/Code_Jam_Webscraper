#include <iostream>
#include <string>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);

	int t=0, t0=0;
	cin>>t;

	while(t0<t)
	{
		string s;
		cin>>s;

		int resp=0;
		if(*s.rbegin()=='-')	resp=1;

		for(int i=s.size()-1; i>0; i--)
		{
			if(s[i]!=s[i-1])	resp++;
		}

		cout<<"Case #"<<t0+1<<": "<<resp<<endl;
		t0++;
	}
}
