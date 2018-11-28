#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int T,tmp,res,x;
	string inp;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		res=x=0;
		cin >> tmp >> inp;
		for(int i=0;i<=tmp;i++)
		{
			if(x<i)
			{
				res+=i-x;
				x=i;
			}
			x+=inp[i]-'0';
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}

