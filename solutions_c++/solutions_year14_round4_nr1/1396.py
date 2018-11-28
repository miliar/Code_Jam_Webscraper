#include<bits/stdc++.h>
using namespace std;
int n,x;
multiset< int,greater<int> > data;
int main()
{
	int T;
	cin>>T;
	for(int no=1;no<=T;no++)
	{
		cin>>n>>x;
		data.clear();
		for(int i=0;i<n;i++)
		{
			int temp;
			cin>>temp;
			data.insert(temp);
		}
		int ans=0;
//		for(multiset<int,greater<int> >::iterator iter=data.begin();iter!=data.end();iter++)
//			cout<<*iter<<endl;
		while(!data.empty())
		{
			if(data.size()>1)
			{
				int now=*data.begin();
				data.erase(data.begin());
//				clog<<*data.lower_bound(x-now)<<endl;
				multiset< int,greater<int> >::iterator lb=data.lower_bound(x-now);
				if(lb!=data.end())
					data.erase(lb);
			}
			else
			{
				data.erase(data.begin());
			}
			ans++;
		}
		printf("Case #%d: %d\n",no,ans);
	}
}

