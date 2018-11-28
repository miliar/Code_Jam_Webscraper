#include <iostream>
#include <algorithm>
using namespace std;
long double a[1200],b[1200];
int n;
void solve()
{
	int i,a_l,b_l,pat1=0,pat2;
	scanf("%d",&n);
	for(i=0;i<n;i++) cin>> a[i];
	for(i=0;i<n;i++) cin>> b[i];
	sort(a,a+n);
	sort(b,b+n);
	a_l=b_l=0;
	while(a_l<n)
	{
		if(a[a_l] > b[b_l])
		{
			pat1++;
			a_l++;
			b_l++;
		}
		else a_l++;
	}
	pat2=n;
	b_l=a_l=0;
	while(b_l<n)
	{
		if(a[a_l] < b[b_l])
		{
			pat2--;
			a_l++;
			b_l++;
		}
		else b_l++;
	}


	printf("%d %d\n",pat1,pat2);
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++) { printf("Case #%d: ",i); solve();}
	return 0;
}