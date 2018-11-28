#include<iostream>
#include<math.h>
#include<string>
#include<stdio.h>
#include<algorithm>
#include<sstream>
using namespace std;
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		int a,b;
		cin>>a>>b;
		int l=ceil(1.0*sqrt(a)),h=floor(1.0*sqrt(b));
		string test1,test2;
		stringstream ss;
		int ret=0;
		for(int i=l;i<=h;i++)
		{
			ss.str("");
			ss<<i;
			test1=ss.str();
			test2=test1;
			reverse(test2.begin(),test2.end());
			if(test1!=test2) continue;
			long long s=i*i;
			ss.str("");
			stringstream ss;
			ss<<s;
			test1=ss.str();
			test2=test1;
			reverse(test2.begin(),test2.end());
			if(test1==test2) ret++;
		}
		cout<<"Case #"<<tt<<": "<<ret<<endl;
	}
	return 0;
}
