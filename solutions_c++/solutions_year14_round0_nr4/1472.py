/*	ashish1610	*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int tcase=1;tcase<=t;++tcase)
	{
		int n;
		cin>>n;
		double naomi_blocks[n],ken_blocks[n];
		for(int i=0;i<n;++i)
			cin>>naomi_blocks[i];
		for(int j=0;j<n;++j)
			cin>>ken_blocks[j];
		sort(ken_blocks,ken_blocks+n);
		sort(naomi_blocks,naomi_blocks+n);
		int ans1=0,ans2=n,index_naomi=0,index_ken=0;
		/*	war	*/
		while(index_naomi<n)
		{
			if(index_ken==n)
				break;
			if(naomi_blocks[index_naomi]<ken_blocks[index_ken])
			{
				ans2--;
				index_naomi++;
			}
			index_ken++;
		}
		index_naomi=0,index_ken=0;
		/*	deceitful war	*/
		while(index_naomi<n)
		{
			if(naomi_blocks[index_naomi]>ken_blocks[index_ken])
			{
				ans1++;
				index_ken++;
			}
			index_naomi++;
		}
		cout<<"Case #"<<tcase<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}
