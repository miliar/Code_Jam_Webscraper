#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		string pancakes;
		cin>>pancakes;
		int res=0;
		char last='+';
		for(int j=pancakes.length()-1;j>=0;j--)
		{
			if(pancakes[j]!=last)
			{
				res++;
				last=pancakes[j];
			}
		}
		cout<<"Case #"<<i<<": "<<res<<endl;
	}
}