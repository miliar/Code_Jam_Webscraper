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
#include<queue>
#include<vector>
#include<algorithm>
#include<string>
#include<climits>
#include<cmath>
using namespace std;
int main()
{
	int t,k=0;
	double c,f,x,fac,tott,totc,diffc,difft,difr,buyfr,buyft,curr;
	scanf("%d",&t);
	while(t--)
	{
		fac=0.0;
		tott=0.0;
		totc=0.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		while(1==1)
		{
			diffc=x;
			difr=2+fac*f;
			difft=diffc/difr;

			buyft=c/difr;
			buyfr=difr+f;
			buyft+=diffc/buyfr;
			//cout<<fac<<": "<<buyft<<" "<<difft<<endl;
			//cout<<fac<<endl;
			if(buyft<difft)
			{
				curr=2+fac*f;
				tott+=c/curr;
				fac++;
			}
			else
			{
				curr=2+fac*f;
				tott+=x/curr;
				break;
			}
		}
		k++;
		printf("Case #%d: %0.7lf\n",k,tott);
	}

	return 0;
}

