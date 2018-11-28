#include<iostream>
#include<cstdlib>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;


int main()
{
	ios_base::sync_with_stdio(0);
	int T;
	cin>>T;

	for(int tt=0; tt<T; tt++)
	{
		int N, c, sa, sb, ca, cb;
		cin>>N;

		string a, b;
		cin>>a>>b;

		bool check=true;

		string x="", y="";
		x+=a[0], y+=b[0];

		for(int i=1; i<a.size(); i++)
		{
			if(a[i]!=a[i - 1])
				x+=a[i];
		}

		for(int i=1; i<b.size(); i++)
		{
			if(b[i]!=b[i - 1])
				y+=b[i];
		}

		if(x==y)
			check=false;
		else
			check=true;

		cout <<"Case #"<<tt+1<< ": ";

		if(check)
		{
			cout << "Fegla Won";
			goto D;
		}
			c=0, sa=0, sb=0;

			for(int i=0; i<x.size(); i++)
			{
				char g=x[i];

				ca=0, cb=0;

				while(sa<a.size() && a[sa]==g)
				{
					ca++;
					sa++;
				}

				while(sb<b.size() && b[sb]==g)
				{
					cb++;
					sb++;
				}

				c+=abs(ca - cb);
			}

			cout << c;
		D:
        cout<<endl;
	}

	return 0;
}

