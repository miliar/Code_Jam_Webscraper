#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int kk = 1;
	while(t--)
	{
		cout<<"Case #"<<kk<<": ";
		kk++;
		int k,c,s;
		cin>>k>>c>>s;
		int req = ceil(k*1.0/2);
		if(k == 1)
		{
			cout<<"1"<<endl;
		}
		else if(c == 1)
		{
			if(s < k)
			{
				cout<<"IMPOSSIBLE"<<endl;
			}
			else
			{
				for(int i=0;i<k;i++)
				{
					cout<<(i+1)<<" ";
				}
				cout<<endl;
			}
		}
		else if(s < req)
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			int r  = 0;
			for(int i=0;i<req;i++)
			{
				if(i == (req -1) && k%2 == 1)
					cout<<(k*r + k);
				else
				cout<<(k*r + (r+2))<<" ";
				r += 2;
			}
			cout<<endl;
		}
	}
	return 0;
}