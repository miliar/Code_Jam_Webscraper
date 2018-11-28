#include<bits/stdc++.h>
using namespace std;

int main()
{
	double t,c,f,x,i,r,test,sum,ans,prev;
//	vector<double> v;
	scanf("%lf",&test);
	for(t=1;t<=test;t++)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		r=2.0;
		ans = x/2.0;
		prev=0.0;
	//	v.clear();
		while(1)
		{
			sum=0.0;
			/*for(i=0;i<v.size();i++)
			{
				sum=sum+(c/(double)v[i]);
			}*/
			sum=sum+prev;
			sum=sum+(x/(double)r);
			prev=prev+((c/(double)r));
			//v.push_back(r);
			if(sum>ans)
				break;
			ans=sum;
			r=r+f;
		}
		printf("Case #");
		cout<<t<<": ";
		printf("%.7f\n",ans);
	}
	return 0;
}
