#include <fstream>
#include <iostream>
using namespace std;

int count(int a,int b, int c)
{
	int r=0;
	for(int i=0;i<a;i++)
	{
		for(int j=0;j<b;j++)
		{
			int k=(i+1+j+1)%c;
			if(k==0)
				r++;
		}
	}
	return r;
}
int main()
{
	ifstream cin("A-small-attempt2.in");
	ofstream cout("A-small-attempt2.out");
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int a,b,c;
		cin>>a>>b>>c;
		int r=b/c;
		if(b%c==0)
			r+=(c-1);
		else
			r+=c;
		//if(c==1)
			//r--;
		cout<<"Case #"<<i+1<<": "<<r<<endl;
	}
	cin.close();
	cout.close();
}
