#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
using namespace std;
int main()
{
	ifstream cin("inb.txt");
	ofstream cout("outb.txt");
	int a,b,k,t,tc,i,ans,ai,bi;
	cin>>t;
	for (tc=1;tc<=t;tc++)
	{
		ans=0;
		cin>>a>>b>>k;
		for (i=0;i<k;i++)
		{
			for (ai=0;ai<a;ai++)
			{
				for (bi=0;bi<b;bi++)
				{
	//				cout<<ai<<" "<<bi<<" "<<(ai&bi)<<" "<<i<<endl;
					if ((ai&bi)==i) ans++;
				}
			}
		}
		cout<<"Case #"<<tc<<": "<<ans<<endl;
	}
}
