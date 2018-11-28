#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include <iostream>
using namespace std;
int main() {
	int t;
	cin>>t;
	for(int ii=1;ii<=t;ii++)
	{
		int n;
		scanf("%d",&n);
		double a[n+1],b[n+1],a1[n+1],b1[n+1];
		for(int i=0;i<n;i++)
		{
			cin>>a[i];
			a1[i]=a[i];
		}
		for(int i=0;i<n;i++)
		{
			cin>>b[i];b1[i]=b[i];
		}
		sort(b1,b1+n);
		sort(a1,a1+n);
		int count=0, visit[11]={0}, ans=-1;
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
			{
				while(j<n&&a1[i]>b1[j])j++;
				while(j<n&&visit[j]==1)j++;
				if(j!=n){visit[j]=1;break;}
			}
		for(int i=0;i<n;i++)
		{
			if(visit[i])
				count++;
		}
		int ans2=n-count,anss=-1;
		for(int i=0;i<11;i++)
			visit[i]=0;
		for(int i=0;i<n;i++)
		{
			int j=n-1;
			while(j>=0&&visit[j]==1)j--;
			if(j!=-1&&a1[i]<b1[j]){
				int count2=0;
				for(int i2=i,j2=0;i2<n;i2++,j2++)
					if((a1[i2]>b1[j2])&&visit[j2]==0)count2++;
				visit[j]=1;
				anss=max(anss,count2);
			}
		}
		count=0;
		int ans1;
		for(int i=0;i<n;i++)
			if(visit[i])
				count++;
		ans1=max(anss,n-count);
		cout<<"Case #"<<ii<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}
