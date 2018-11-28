#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<map>
#include<vector>
#include<cstdio>
#include<climits>
#include<cmath>
#include<cstring>
#define mod 1000000009
using namespace std;

int main()
{
	/*freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);*/
	double t,c,f,x,i,j,k,rate,temp,ans;
	vector< double > v;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>c>>f>>x;
		rate=2.0;
		ans = x/2.0;v.clear();
		while(1)
		{
			temp=0.0;
			for(i=0;i<v.size();i++)
			{
				temp=temp+(c/(double)v[i]);
			}
			temp+=(x/(double)rate);
			v.push_back(rate);
			if(temp>ans)
				break;
			ans=temp;
			rate+=f;
			//cout<<temp<<" ";
		}
		cout<<"Case #"<<k<<": ";
		printf("%.7f\n",ans);
	}
	return 0;
}