#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main() {
    freopen("D-large.in", "rt", stdin);
    freopen("D-large.out", "wt", stdout);
	int tc,n,st1,st2,wc,dwc,st11,st22,end11,end22;
	double a[1500],b[1500];
	scanf("%d",&tc);
	for(int y=1;y<=tc;y++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for(int i=0;i<n;i++)
			scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		st1=st2=n-1;
		st11=st22=n-1;
		end11=end22=0;
		wc=dwc=0;
		/******solving*******/
		for(int i=n-1;i>=0;i--)
		{
			/**********WAR************/
			if(a[st1]>b[st2])
				wc++;
			else
				st2--;
			st1--;
			/*******DECEIT WAR********/
			if(a[end11]>b[end22])
			{
				dwc++;
				end22++;
			}
			end11++;
		}
		printf("Case #%d: %d %d\n",y,dwc,wc);
	}
	return 0;
}
