#include<bits/stdc++.h>
using namespace std;

#define MAX 1050
int compute(int count[],int d);

int main()
{
	int t,p;
	int count[MAX],d;

	scanf("%d",&t);
	for(int tst=1;tst<=t;tst++)
	{
		scanf("%d",&d);

		for(int i=0;i<=100;i++)
            count[i] = 0;

		for(int i=0;i<d;i++)
		{
			scanf("%d",&p);
			count[p] = count[p]+1;
		}
		printf("Case #%d: %d\n",tst,compute(count,d));
	}
	return 0;
}


//brute force algorithm
int compute(int count[],int d)
{
	int pos=0;
	//finding the biggest element if it exists
	
	for(int i=10;i>=1;i--)
	{
		if(count[i]>0)
			pos=i;

        if(pos!=0)
            break;
	}
	if(pos<=3) return pos;
	int result = pos;

	for(int i=1;i<pos;i++)
	{
	    int temp = count[pos];

	    //assumption
		count[pos]=0;
		count[i]= count[i] + temp;
		count[pos-i]= count[pos-i] + temp;
		result=min(result,temp+compute(count,d));

		//backtrack
		count[i]=  count[i] - temp;
		count[pos-i]= count[pos-i] - temp;
		count[pos] = temp;
	}
	return result;
}
