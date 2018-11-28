#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
#define min(a,b) ((a) < (b) ? (a) : (b))
int main() {
	int t,l,i;
	cin>>t;
	l=t;
	while(t--)
	{
		int n,i,ansa=0,ansb=0;
		cin>>n;
		vector <double> a,b,c,d;
		for(i=0;i<n;i++)
		{
		double o;
		cin>>o;
		a.push_back(o);
		c.push_back(o);
		}
		sort(a.begin(),a.begin()+n);
		sort(c.begin(),c.begin()+n);
		for(i=0;i<n;i++)
		{
		double o;
		cin>>o;
		b.push_back(o);
		d.push_back(o);
		}
		sort(b.begin(),b.begin()+n);
		sort(d.begin(),d.begin()+n);
		int k=n-1;
		while(k>-1)
		{
			if(c[k]>d[k])
			{
				ansb++;
				c.erase(c.begin()+k);
				d.erase(d.begin());
				k--;
			}
			else
			{
				int j=k-1;
				while(j>-1&&c[k-1]<d[j-1])
				j--;
				c.erase(c.begin()+k);
				d.erase(d.begin()+j+1);
				k--;
			}
		}
		k=n-1;
		while(k>-1)
		{
			int j;
			if(a[0]<b[0])
			{
				a.erase(a.begin());
				b.erase(b.begin()+k);
				k--;
			}
			else
			{
				j=k;
				while(a[0]<b[j])
				j--;
				ansa++;
				a.erase(a.begin());
				b.erase(b.begin()+j);
				k--;
			}
		}
		cout<<"Case #"<<l-t<<": "<<ansa<<" "<<ansb<<endl;
	}
	return 0;
}