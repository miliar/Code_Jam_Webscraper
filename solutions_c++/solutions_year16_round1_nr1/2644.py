#include<bits/stdc++.h>
using namespace std;
#define lli long long int
int main(int argc, char const *argv[])
{
	int n;
	cin>>n;
	for (int j = 0; j < n; ++j)
	{
		string x;
		cin>>x;

		string y;
		y=x[0];
		for (int i = 1; i < x.length(); ++i)
		{
			if(x[i]>=y[0]) y=x[i]+y;
			else y = y+x[i];
		}
		cout<<"Case #"<<j+1<<": "<<y<<endl;
	}
	return 0;
}