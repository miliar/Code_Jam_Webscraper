#include <iostream>
#include <cstdio>
using namespace std;


int main()
{
	int t,max,count,n,req,t1,ava;
	char shy;
	freopen("sol.txt", "w", stdout);
	freopen("test.txt", "r", stdin);
	cin>>t;
	t1  = t;
	while(t--)
	{
		count = 0;
		n = 0;
		req = 0;
		ava = 0;
		cin>>max;
		getchar();
		count = getchar() - '0';
		while(max--)
		{
			req++;
			ava = getchar() - '0';
			if(count < req)
			{
				n = n + req - count;
				count = req;
			}
			count = count + ava;
		}
		cout<<"Case #"<<t1-t<<": "<<n<<endl;
	}
	return 0;
}
