#include<iostream>
#include<string>
#define si(n) scanf("%d",&n)
#define pi(n) printf("%d\n",n)
#include<math.h>
#include<algorithm>
using namespace std;
int main()
{
	freopen("input-A.txt","r",stdin);
	freopen("output-A.txt","w",stdout);
	int t;si(t);
	int k = 1;
	while(t--)
	{
		int s;
		si(s);
		string arr;
		cin>>arr;
		int ans = 0;
		int sum = 0;
		for(int i=0;i<=s;i++)
		{
			 if(sum<i)
			 {
			 	int k = i-sum;
			 	ans+=k;
			 	sum+=k;
			 }
			 //cout<<sum<<" "<<ans<<endl;
			 sum+=arr[i]-'0';
		}
		printf("Case #%d: %d\n",k++,ans);
	}
}
