#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<cmath>
#include<set>
#include<fstream>
using namespace std;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t,ans,dumm,x;
	cin>>t;
	vector<int> v;
	vector<int> final;
	for(int tc=1;tc<=t;tc++)
	{
		v.clear();
		final.clear();
		cin>>ans;
		for(int i=1;i<=4;i++)
		{
			if(i!=ans)
			{
				cin>>dumm>>dumm>>dumm>>dumm;
			}
			else
			{
				for(int j=1;j<=4;j++)
				{
					cin>>x;
					v.push_back(x);
				}
			}
		}

		int res=0;
		cin>>ans;
		sort(v.begin(),v.end());

		for(int i=1;i<=4;i++)
		{
			if(i!=ans)
			{
				cin>>dumm>>dumm>>dumm>>dumm;
			}
			else
			{
				for(int j=1;j<=4;j++)
				{
					cin>>x;
					if(binary_search(v.begin(),v.end(),x))
						final.push_back(x);
				}
			}
		}

		cout<<"Case #"<<tc<<": ";

		if(final.size() ==0)
			cout<<"Volunteer cheated!"<<endl;
		else if(final.size()==1)
			cout<<final[0]<<endl;
		else
			cout<<"Bad magician!"<<endl;
	}
	return 0;
}


