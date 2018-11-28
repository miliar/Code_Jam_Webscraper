#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Ohyeah.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		string st,res="";
		cin>>st;
		for(int j=0;j<st.length();j++)
		{
			if(j==0)	res += st[j];
			else
			{
				if(st[j]>=res[0])
					res=st[j]+res;
				else
					res=res+st[j];
			}
		}
		cout<<"Case #"<<i<<": "<<res<<endl;
	}
	return 0;
}
