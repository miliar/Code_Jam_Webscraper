// QualRound.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include "iostream"
#include "string"
#include "string.h"
#include "vector"
#include "algorithm"
using namespace std;

int main()
{
 //	freopen("D-small-attempt0.in","r",stdin);
	//freopen("D-small-attempt0.out","w",stdout);
	freopen("D-Large.in","r",stdin);
	freopen("D-Large.out","w",stdout);
	int T=0;
	cin>>T;
	for(int tc=0;tc<T;tc++)
	{
		int N;
		cin>>N;
		vector<int> s,t;
		for(int i=0;i<N;i++)
		{
			double d;
			cin>>d;
			int k=(d+1e-7)*100000;
			s.push_back(k);
		}
		for(int i=0;i<N;i++)
		{
			double d;
			cin>>d;
			int k=(d+1e-7)*100000;
			t.push_back(k);
		}
		sort(s.begin(),s.end());
		sort(t.begin(),t.end());
		int ans1=0;
		int cur=0;
		for(int i=0;i<N;i++)
		{
			if(s[i]>t[cur])
			{
				ans1++;
				cur++;
			}
		}
		sort(t.begin(),t.end());
		cur=0;
		int ans2=0;
		for(int i=0;i<N;i++)
		{
			if(t[i]>s[cur])
			{
				cur++;
				ans2++;
			}
		}
		cout<<"Case #"<<tc+1<<": "<<ans1<<" "<<N-ans2<<endl;
	}
	return 0;
}