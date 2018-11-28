#include<cstdio>
#include<vector>
#include<cstdlib>
#include<string>
using namespace std;
int check(string str)
{
	int i=0,j=str.size()-1;
	while(i<=j)
	{
		if(str[i++]!=str[j--])
		{
			return 0;
		}
	}
	return 1;
}
int count(vector<int> arr,int a,int b)
{
	int c=0;
	int lim=arr.size();
	for(int i=0;i<lim;++i)
	{
		if(a-arr[i]<=0&&b-arr[i]>=0)
			c++;
	}
	return c;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("d.txt","w",stdout);
	int t=0;
	scanf("%d",&t);
	vector<int> ans;
	for(int i=1;i<=32;++i)
	{
		char temp[100];
		itoa(i,temp,10);
		string str(temp);
		if(check(str))
		{
			itoa(i*i,temp,10);
			str=temp;
			if(check(str))
				ans.push_back(i*i);
		}
	}
	for(int k=0;k<t;++k)
	{
		int a=0,b=0;
		scanf("%d %d",&a,&b);
		printf("Case #%d: %d\n",k+1,count(ans,a,b));
	}
	return 0;
}