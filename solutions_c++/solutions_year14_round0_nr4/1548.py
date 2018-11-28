#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;
const int MAXLEN = 2000; 
int T,N;
double niomi[MAXLEN],ken[MAXLEN];
int dp[MAXLEN][MAXLEN];
bool cmp(const double &a,const double &b)
{
	return a<b;
}

int war()
{
	int index1=0,index2=0,res=0;
	while (index1<N && index2<N)
	{
		while (ken[index2]<niomi[index1] && index2<N)
		{
			index2++;
		}
		if (index2<N && ken[index2]>niomi[index1])
		{
			index1++;
			index2++;
		}
	}
	return N-index1;
}

int dwar()
{
	int index1=0,index2=0,res=0;
	for (; index1<N; index1++)
	{
		if (niomi[index1]>ken[index2])
		{
			res++;
			index2++;
		}
	}
	return res;
}

int main(int argc, char *argv[])
{
	scanf("%d",&T);
	int cases = 0;
	while (cases <T)
	{
		cases++;
		cin>>N;
		for (int i=0; i<N; i++)
		{
			cin>>niomi[i];
		}
		for (int i=0; i<N; i++)
		{
			cin>>ken[i];
		}
		sort(niomi,niomi+N,cmp);
		sort(ken,ken+N,cmp);
		int res1,res2;
		res1 = war();
		res2 = dwar();
		printf("Case #%d: %d %d\n",cases,res2,res1);
	}
	
	return 0;
}
