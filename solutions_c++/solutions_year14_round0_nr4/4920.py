#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string.h>
#include<map>
#include<cmath>
#include<iomanip>
#include<vector>
#include<queue>
using namespace std;
typedef long long LL;



int main(){
	int t;
	scanf("%d",&t);
	int z=t;
	while(t--)
	{
		int n,c=0,cnt=0,k=0;
		scanf("%d",&n);
		double a[n],b[n];
		for(int i=0;i<n;i++)
		{
			scanf("%lf",&a[i]);
		}
		for(int i=0;i<n;i++)
		{
			scanf("%lf",&b[i]);
			
		}
		sort(a+0,a+n);
		sort(b+0,b+n);
		for(int i=0;i<n&&k<n;i++)
		{
				if(a[i]>b[k])
				{
					
					c++;
					k++;
				}
		}
		k=0;
		for(int i=0;i<n;i++)
		{
			if(a[k]<b[i])
			{
				cnt++;
				k++;
			}
		}
		cout<<"Case #"<<z-t<<": "<<c<<" "<<n-cnt<<endl;
	}
	   
    return 0;
}
