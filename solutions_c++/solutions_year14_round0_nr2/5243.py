#include<iostream>
#include<string>
using namespace std;



int main()
{
	freopen("B-large.in","r",stdin);

	freopen("out.in","w",stdout);
	int t,count=0;
	cin>>t;
	while (t--)
	{

		count++;
		long double c,f,x,sum=0;
		cin>>c>>f>>x;
		for(long double step=2;;step+=f)
		{
			if(sum + c/step + x/(step+f) >= sum + x/step )
			{
				sum+=x/step;  break;
			}
			sum+=c/step;
		}
		printf("Case #%d: %.7f\n",count,sum);
	}
}