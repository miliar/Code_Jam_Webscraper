#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;
int main()
{	int i,t,j,n,dw1,dw2,dw3,dw4,w,k;
	vector<double> a,b,a1,b1;
	double temp;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{	dw1=dw2=dw3=dw4=w=0;
		scanf("%d",&n);
		//a=(int *)malloc(n*sizeof(double));
		//b=(int *)malloc(n*sizeof(double));
		for(j=0;j<n;j++){
		scanf("%lf",&temp);
		a.push_back(temp);
		a1.push_back(temp);
		}

		for(j=0;j<n;j++){
		scanf("%lf",&temp);
		b.push_back(temp);
		b1.push_back(temp);
		}
		sort(a.begin(),a.end());
		sort(a1.rbegin(),a1.rend());
		sort(b.begin(),b.end());
		sort(b1.rbegin(),b1.rend());
		int pos=0;				
		for(j=0;j<n;j++)
		{	
			if(a1[j]>b1[j])
				dw1++;
			if(a1[j]>b[j])
				dw2++;	
			if(a[j]>b1[j])
				dw3++;
			for(k=pos;k<n;k++)
			{	if(a[j]<b[k])
				{	w++;
					pos=k+1;
					break;
				}
			}
							
		}
		pos=0;
		for(j=0;j<n;j++)
			for(k=pos;k<n;k++)
			{	if(b[j]<a[k])
				{	dw4++;
					pos=k+1;
					break;
				}
			}
		printf("Case #%d: %d %d\n",i,max(max(dw1,dw4),max(dw2,dw3)),n-w);
		a.clear();
		b.clear();
		a1.clear();
		b1.clear();
	}
	return 0;
}
	
