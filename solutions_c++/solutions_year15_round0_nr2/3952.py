#include<iostream>
#include<cstdlib>

using namespace std;

int count(int a[],int max,int min,int time)
{
	int it;
	for(it=max;it>0;it--)
	{
		if(a[it]==0)
			continue;
		int temp=(it+1)/2;
		if(it+time<min)
		{
			min=it+time;
			//cout<<it<<" "<<time<<" "<<max<<endl;
		}
		if(a[it]<temp)
		{
			int timetemp=a[it];
			if(time+timetemp<it)
			{
				time+=timetemp;
				for(int x=temp;x<it;x++)
				{
					a[x]+=a[it];
					a[it-x]+=a[it];
					int temp2=count(a,it-1,min,time);
					if(temp2<min)
					{
						min=temp2;
					}
					a[x]-=a[it];
					a[it-x]-=a[it];
				}
				return min;
			}
			else
			{
				return min;
			}
		}
		else
		{
			return min;
		}
	}
}

int main()
{
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		int a[1001],it;
		for(it=1;it<=1000;it++)
			a[it]=0;
		int d,p,max=0;
		cin>>d;
		for(it=0;it<d;it++)
		{
			cin>>p;
			if(p>max)
				max=p;
			a[p]++;
		}
		int time=0,min=10001;
		if(a[max]>=(max+1)/2)
			min=max;
		else
		{
			time=a[max];
			min=max;
			for(it=(max+1)/2;it<max;it++)
			{
				a[it]+=a[max];
				a[max-it]+=a[max];
				int temp=count(a,max-1,min,time);
				if(temp<min)
				{
					min=temp;
				}
				a[it]-=a[max];
				a[max-it]-=a[max];
			}
		}
		cout<<"Case #"<<i<<": "<<min<<endl;
	}
	return 0;
}
