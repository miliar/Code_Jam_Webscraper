#include <bits/stdc++.h>

using namespace std;

int main()
{	std::ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int ti=1;ti<=t;ti++)
	{	long long int n;
		cin>>n;
		bool* found=new bool[10];
		for(int i=0;i<10;i++)found[i]=false;
		long long int tocheck=0,tmp;
		bool done=false;
		for(int i=0;i<1000000;i++)
		{	tocheck+=n;
			tmp=tocheck;
			stringstream tmpstr;
			tmpstr<<tocheck;
			string tmps=tmpstr.str();
			for(int j=0;j<tmps.length();j++)
			{	found[(tmps[j]-'0')]=true;
			}
			bool donetmp=true;
			for(int j=0;j<10;j++)
			{	if(!found[j])donetmp=false;
			}
			if(donetmp)
			{	done=true;
				break;
			}
		}
		cout<<"Case #"<<ti<<": ";
		if(!done)cout<<"INSOMNIA"<<endl;
		else cout<<tocheck<<endl;
	}
}
