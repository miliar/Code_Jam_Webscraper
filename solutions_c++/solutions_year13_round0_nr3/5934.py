#include<iostream>
#include<math.h>

using namespace std;

int main()
{
	int t,q;
	cin>>t;
	q=t;
	while(t--)
	{
		int a,s,count=0;
		cin>>a>>s;
		for(int i=a;i<=s;i++)
		{
			int n,ri=0;
			n = i;
			do
			{
				ri = ri*10 + (n%10);
				n=n/10;
			}while(n>0);
			if(ri == i)
			{
				int sq = int(sqrt(double(i)));
				int rsq=0;
				n = sq;
				do
				{
					rsq = rsq*10 + (n%10);
					n=n/10;

				}while(n>0);
				if(rsq == sq && pow(sq,2) == i)
					count++;
			}


		}
		cout<<"Case #"<<(q-t)<<": "<<count<<endl;
		
	}

	return 0;
}
