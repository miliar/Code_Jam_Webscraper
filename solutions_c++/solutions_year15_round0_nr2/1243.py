#include<stdio.h>
#include<string.h>

int P[1001];
int DP(int numberOfCakes)
{
	if(numberOfCakes<=2)
		return numberOfCakes;
	int timeTaken = P[numberOfCakes];
	int limit = numberOfCakes/2;
	int index = 0;
	int Value = numberOfCakes;
	int gValue = numberOfCakes;
	for(int noC = numberOfCakes-1;noC>=limit;noC--)
	{
		P[noC] += timeTaken;
		P[numberOfCakes - noC] += timeTaken;
		int i;
		for(i = numberOfCakes-1;i>=1;i--)
		{
			if(P[i])
				break;
		}
		Value = timeTaken + DP(i);
		if(gValue > Value)
		{
			gValue = Value;
			index = noC;
		}
		P[noC] -= timeTaken;
		P[numberOfCakes - noC] -= timeTaken;
	}
	return gValue;
}

int main()
{
	int T,D,val,mx;
	freopen ("D:\\Input.txt","rb",stdin);
	freopen ("D:\\Output1.txt","wb",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		scanf("%d",&D);
		memset(P,0,4004);
		mx = 0;
		for(int j=1;j<=D;j++)
		{
			scanf("%d",&val);
			P[val]++;
			if(mx < val)
				mx = val;
		}
		printf("Case #%d: %d\n",i,DP(mx));
	}
	return 0;
}
