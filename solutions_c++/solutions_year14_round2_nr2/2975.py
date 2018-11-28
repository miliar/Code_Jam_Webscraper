#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<set>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;

	for (int x = 1; x <= T; x++)
	{
		long a,b,k;
		cin>>a>>b>>k;
		int counter=0;
		for (int i = 0; i < a; i++)
		{
			for (int j = 0; j < b; j++)
			{
				long out  = i &j;
				if(out<k)
					counter++;
			}
		}
		cout<<"Case #"<<x<<": "<<counter<<endl;
	}
	return 0;
}