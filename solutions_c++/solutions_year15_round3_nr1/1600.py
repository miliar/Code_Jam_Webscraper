#include<bits/stdc++.h>
using namespace std;
int main()
{
	int T,r,c,w;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		scanf("%d %d %d", &r, &c, &w);
		int cpy=c;
		int ans=0;
		while(cpy>w)
		{
			int k=0;
			
			while((k<=w) && (cpy-k)>=w)
			k++;
			
			k--;
			//cout<<k<<endl;
			//int x;
			//cin>>x;
			cpy-=k;
			ans++;
		}
		ans+=w;
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
