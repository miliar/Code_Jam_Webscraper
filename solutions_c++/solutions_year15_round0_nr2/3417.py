#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<queue>
using namespace std;
int minstep(int num, int req)
{
	if(num <= req)return 0;
	return (num-1)/req;

}
int main()
{
	int t;
	cin>>t;
	for(int q=1;q<=t;++q)
	{
		int ans=1000000;
		int d,x;
		cin>>d;
		priority_queue<int> pc;
		for(int i=0;i<d;++i){cin>>x;pc.push(x);}
		for(int mpc = 1;mpc <= 1003;++mpc)
		{
			int lans=0;
			priority_queue<int> now=pc;
			while(!now.empty())
			{
				int mc = now.top();
				now.pop();
				if(mc<=mpc)
				{
					break;
				}
				lans+=minstep(mc,mpc);
			}
			ans=min(ans,lans+mpc);
		}
		cout<<"Case #"<<q<<": "<<ans<<endl;
	}
	return 0;
}
