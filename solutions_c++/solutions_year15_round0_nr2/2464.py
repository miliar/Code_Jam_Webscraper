#include <iostream>
#include <algorithm>
using namespace std;
int const N = 1005;
int T[N];
int main()
{
	ios_base::sync_with_stdio(0);
	int z;
	cin>>z;
	for(int x=1;x<=z;x++)
	{
		int n;
		cin>>n;
		for (int i=0;i<n;i++)
		{
			cin>>T[i];
		}
		sort(T,T+n);
		int maxa = T[n-1];
		int wyn=1000000;
		int wync=0;
		for (int k=1;k<=maxa;k++)
		{
			wync=0;
			for (int i=0;i<n;i++)
			{
				if(T[i]>k)wync+=((T[i]/k) + ((T[i]%k > 0)-1));
			}
			wync+=k;
			wyn = min(wync,wyn);
		}
		cout<<"Case #"<<x<<": "<<wyn<<endl;
	}
}
