#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;
struct PR3
{
	int sum,x,y;
}tmp,list[100010];
bool operator <(const struct PR3& a,const struct PR3& b)
{
	if(a.sum-b.sum)
		return a.sum>b.sum;
	else if (a.x-b.x)
		return a.x>b.x;
	else
		return a.y>b.y;
}
int main()
{
	freopen("Ain.in","r",stdin);
	freopen("Aout.txt","w",stdout);
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		int N,X;
		cin>>N;
		int ar[N];
		cin>>X;
		for(int j=0;j<N;j++)
			cin>>ar[j];
		//vector<struct PR3 > list;
		//list.clear();
		int kx=0;
		for(int j=0;j<N;j++)
			for(int k=0;k<j;k++)
				if(ar[j]+ar[k]<=X&&j!=k)
				{
					tmp.sum=ar[j]+ar[k];
					tmp.x=j;
					tmp.y=k;
					list[kx++]=tmp;
				}
		printf("Case #%d: ",i);
		//cout<<list[0].sum<<endl;
		bool v[N];
		memset(v,false,sizeof(v));
		sort(&list[0],&list[kx]);
		long long ans=0;
		for(int i=0;i<kx;i++)
			if(!v[list[i].x]&&!v[list[i].y])
				v[list[i].x]=v[list[i].y]=true,ans++;
		for(int i=0;i<N;i++)
			if(!v[i])
				ans++;
		cout<<ans<<endl;
	}
	return 0;
}
