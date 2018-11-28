#include<stdio.h>
#include<algorithm>
int tab[10004];
using namespace std;
int main()
{
    int zes;
	scanf("%d",&zes);
    for (int z=0;z<zes;z++)
    {
	int n,x;
	scanf("%d%d",&n,&x);
	for (int i =0;i<n;i++)
	    scanf("%d",&tab[i]);
	sort(tab,tab+n);
	int act=0;
	int res=0;
	for (int i =n-1;i>=0;i--)
	{
	    if(i>act)
	    {
	
		int sum = tab[i] + tab[act];
		if(sum<= x)
		{
		    act++;
		}
		res++;
	    }
		else if(i==act)
	    {
		res++;
	    }
	}
	printf("Case #%d: %d\n",z+1,res);
	


    }


}