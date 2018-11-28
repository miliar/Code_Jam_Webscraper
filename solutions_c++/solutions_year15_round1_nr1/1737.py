#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;
int main()
{
//	freopen("in.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=0;t<T;t++)
	{
		cout<<"Case #"<<t+1<<": ";
		int N;
		int res1=0, res2=0;
		int m[20000];
		cin>>N;
		for (int i=0;i<N;i++)
			cin>>m[i];

		int diff, maxdiff=0;
		for (int i=0;i<N-1;i++)
		{
			diff = m[i]-m[i+1];
			if (diff>0)
				res1+=diff;
		}
		for (int i=0;i<N-1;i++)
		{
			diff = m[i]-m[i+1];
			if (diff>maxdiff)
				maxdiff = diff;
		}
		for (int i=0;i<N-1;i++)
		{
			if (m[i]>maxdiff)
				res2+=maxdiff;
			else
				res2+=m[i];
		}
		cout<<res1<<" "<<res2<<endl;
	}
	return 0;
}
