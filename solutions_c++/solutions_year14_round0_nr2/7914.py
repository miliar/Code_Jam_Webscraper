#include<bits/stdc++.h>
using namespace std;
double min(double a, double b)
{
	if((a-b)>0)
	return b;
	else return a;
}
int main()
{
	int t,m;
	scanf("%d",&t);
	for(m=1;m<=t;m++)
	{
		double c,f,x,sum=0.0,q=0.0,k;
		cin>>c>>f>>x;
		double ctr=2.0;
		double ans=x/ctr;
		if(x<=c)		
		printf("Case #%d: %0.7lf\n",m,x/2);
		
		else{
		while((x-q)>c)
		{
		   k=(double)c/ctr;
		   sum+=k;
		   
		   q+=c;
		   ans=min(ans,sum+x/(ctr+f));
		   ctr+=f;
		}
		printf("Case #%d: %0.7lf\n",m,ans);
	}
	}
	return 0;
}
/*Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762
*/
