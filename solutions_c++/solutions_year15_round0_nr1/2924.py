#include<bits/stdc++.h>

using namespace std;

int toInt(char ch)
{
	return ch-'0';
}

int main()
{
	int t;
	cin>>t;
	string s;
	int remf,curf,len,req;
	for(int i=0;i<t;++i)
	{
		cin>>len>>s;
		curf = toInt(s[0]);
		req = 0;
		for(int j=1;j<len+1;++j)
		{
			remf =  j - curf;
			if(remf>0 && s[j]>'0')
			{
				req+=remf;
				curf+=remf;
			}
			curf+=toInt(s[j]);
			//cerr<<j<<" "<<remf<<" "<<curf<<endl;
		}
		cout<<"Case #"<<i+1<<": "<<req<<endl;
	}
	return 0;
}
