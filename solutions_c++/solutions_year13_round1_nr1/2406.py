#include<iostream>
using namespace std;


int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);

	int T;
	cin >> T;

	long long r, t, n = 0;
	long long area = 0,remain_paint;

	for(int i = 1; i <= T; i++)
	{
		cin>>r>>t;
		area = ((r+1)*(r+1)) - ((r)*(r));
		remain_paint = t - area;
		n = 1;
		while(true)
		{
			r += 2;
			area = ((r+1)*(r+1)) - ((r)*(r));
			if (remain_paint >= area)
			{
				remain_paint -= area;
				n++;
			}
			else
				break;
		}
		//
		cout<<"Case #"<<i<<": "<<n<<endl;
	}

	return 0;
}
