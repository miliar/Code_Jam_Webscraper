/*
* @Author: deepanshu
* @Date:   2016-05-08 14:11:43
* @Last Modified by:   deepanshu
* @Last Modified time: 2016-05-08 15:05:41
*/
#include <bits/stdc++.h>
using namespace std;
struct S
{
	int val,indi;
};
bool compare(S l,S r){return l.val>r.val;}
int main()
{
	int t,l=1;
	scanf("%d",&t);
	while(l<=t)
	{
		int n,sum=0;
		printf("Case #%d: ",l);
		scanf("%d",&n);
		S a[n];
		for (int i = 0; i < n; ++i)
		{
			scanf("%d",&a[i].val);
			sum+=a[i].val;
			a[i].indi=i;
		}
		sort(a,a+n,compare);
		int i=0;
		while(i<n&&a[i].val!=0)
		{
			/*int diff=sum/2+1 -a[i].val;*/
			a[i].val--;
			sum--;
			printf("%c",a[i].indi+'A');
			sort(a,a+n,compare);
			if(a[0].val==1&&a[1].val==1&&a[2].val==0)
			{
				printf(" ");
			}
			else
			{
				a[i].val--;
				sum--;
				printf("%c ",a[i].indi+'A');
				sort(a,a+n,compare);
			}
		}
		printf("\n");
		l++;
	}
    return 0;
}