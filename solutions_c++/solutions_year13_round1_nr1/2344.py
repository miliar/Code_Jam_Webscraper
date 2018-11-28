#include<cstdio>
#include<iostream>
#include<cassert>
#include<cctype>
#include<cfloat>
#include<climits>
#include<cstring>
#include<bitset>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#include<string>
#include<climits>
#include<cmath>
using namespace std;
int main()
{
	int i,T,f,k;
	double r,t;
	double a,b,c,j,ans,temp1,temp2,d;
	scanf("%d",&T);
	k=0;
	while(T--)
	{
		k++;
		scanf("%lf %lf",&r,&t);
		a=2;
		b=2*r-1;
		c=-t;
		d=b*b-4*a*c;
		if(d==0)
		{
			temp1=-b/(2*a);
			temp2=temp1;
		}
		else
		{
			temp1=(-b+sqrt(d))/(2*a);
			temp2=(-b-sqrt(d))/(2*a);
		}
		//cout<<temp1<<" "<<temp2<<endl;
		ans=max(temp1,temp2);
		f=floor(ans);
		printf("Case #%lld: %lld\n",k,f);
	}

	return 0;
}
