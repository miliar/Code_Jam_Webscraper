#include <bits/stdc++.h>
using namespace std;
#define pb push_back

int main()
{
	int T;
	cin>>T;
	double temp;
	for(int ss=1;ss<=T;ss++)
	{
		int n;
		cin>>n;
		vector <double> v1;
		vector <double> v2;
		for(int i=0;i<n;i++)
		{
			cin>>temp;
			v1.pb(temp);
		}
		for(int i=0;i<n;i++)
		{
			cin>>temp;
			v2.pb(temp);
		}
		int war=0,dis_war=0;
		int p1=0,p2=0;
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		for(int i=0;i<n;i++)
		{
			if(v2[p2]>v1[p1])
			{
				p1++;
				p2++;
			}
			else
			{
				p2++;
				war++;
			}
		}
		p2=0;p1=0;
		for(int i=0;i<n;i++)
		{
			if(v2[p2]<v1[p1])
			{
				p1++;
				p2++;
				dis_war++;
			}
			else
			{
				p1++;
			}
		}
		cout<<"Case #"<<ss<<": "<<dis_war<<" "<<war<<endl;
	}
	return 0;
}
