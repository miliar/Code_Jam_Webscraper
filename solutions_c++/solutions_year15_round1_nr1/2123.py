#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char const *argv[])
{
	int t,n;
	cin>>t;
	for (int it = 1; it <= t; ++it)
	{
		cin>>n;
		vector<int> a(n);
		for (int i = 0; i < n; ++i)
		{
			cin>>a[i];
		}
		int ans1=0,ans2=0,maxdec=0,dec;
		for (int i = 1; i < n; ++i)
		{
			if(a[i]<a[i-1]){
				ans1 += a[i-1] - a[i];
				dec = a[i-1] - a[i];
				if(dec > maxdec)
					maxdec = dec;
			}
		}
		dec = maxdec/10;
		for (int i = 1; i < n; ++i)
		{
			if(a[i-1]<maxdec){
				ans2 += a[i-1] ;
			}
			else
				ans2 += maxdec;
		}
		cout<<"Case #"<<it<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}