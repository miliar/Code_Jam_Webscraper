#include<cstdio>
#include<vector>
#include<cmath>
#include<vector>
using namespace std;

bool ispal(int n)
{
	vector<int> a;
	while(n!=0)
	{
		a.push_back(n%10);
		n/=10;
	}
	for(int i=0,j=a.size()-1;i<=j;i++,j--)
		if(a[i]!=a[j])
			return false;
	return true;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int ix=1;ix<=t;ix++)
	{
		int m,n;
		scanf("%d %d",&m,&n);
		int count=0;
		for(int i=(int)sqrt(m);i*i<=n;i++)
		{
			if(ispal(i)&&ispal(i*i)&&i*i>=m)
				count++;
		}
		printf("Case #%d: %d\n",ix,count);
	}
	return 0;
}