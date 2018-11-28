#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,test,n,i,j,count,count1;
  //  freopen("input.txt","r",stdin);
	vector< double >v,w;
	cin>>test;
	for(t=1;t<=test;t++)
	{
		cin>>n;
		count=0;
		count1=0;
		v.resize(n);
		w.resize(n);
		for(i=0;i<n;i++)
		{
			cin>>v[i];
		}
		sort(v.begin(),v.end());
		for(i=0;i<n;i++)
		{
			cin>>w[i];	
		}
		sort(w.begin(),w.end());
		for(i=0,j=0;i<v.size() && j<w.size();)
		{
			if(v[i]>w[j])
			{
				i++;
				j++;
				count1++;
			}
			else
				i++;
		}
		for(i=v.size()-1;i>=0;i--)
		{
			bool flag=0;
			for(j=0;j<w.size();j++)
			{
				if(w[j]>v[i])
				{
					w[j]=-w[j];
					flag=1;
					break;
				}
			}
			if(flag==0)
			{
				count++;
				for(j=0;j<n;j++)
				{
					if(w[j]>0)
					{
						w[j]=-w[j];
						break;
					}
				}
			}
		}
		cout<<"Case #"<<t<<": "<<count1<<" "<<count<<endl;
	}
	return 0;
}
