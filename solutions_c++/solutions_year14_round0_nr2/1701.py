/*	ashish1610	*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int tcase=1;tcase<=t;++tcase)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double const_cook=2;
		double ans=0.0,mark=0,temp,temp1,temp2;
		while(mark!=x)
		{
			temp=x/const_cook;
			temp1=c/const_cook;
			temp2=x/(const_cook+f);
			if((temp1+temp2)<temp)
			{
				const_cook+=f;
				ans+=temp1;
			}
			else
			{
				mark=x;
				ans+=temp;
			}
			
		}
		/*if(x<2*c)
		{
			ans=x/const_cook;
		}
		else
		{
			int cnt=x/c;
			for(int i=0;i<cnt-1;++i)
			{
				ans=ans+(c/const_cook);
				const_cook+=f;
			}
			ans=ans+x/const_cook;
		}*/
		cout<<"Case #"<<tcase<<": ";
		printf("%.7f\n",ans);
		//cout<<ans<<endl;
	}
	return 0;
}
