#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define mod 1000000007
int main()
{
	int t,r,c,w;
	int x=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&r,&c,&w);
		cout<<"Case #"<<x++<<": ";
		
		int ans=(c/w)*(r-1)+(c/w)+w-1;
		if(c%w)
			ans++;
		cout<<ans<<endl;
	}
	return 0;
}