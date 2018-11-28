#include<cctype>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<deque>
using namespace std;

int N;
deque<int> Q1,Q2;

int solve1()
{
	int ret=0;
	for(int i=0;i<N;i++)
	{
		if(Q1[i]<Q2.front())Q2.pop_back();
		else{Q2.pop_front();ret++;}
	}
	Q1.clear();
	return ret;
}

int solve2()
{
	int j=0,k=0;
	for(int i=0;i<N;i++)
	{
		while(j<N&&Q2[j]<=Q1[i])j++;
		if(j<N){j++;k++;}
	}
	return N-k;
}

void input(deque<int> &Q)
{
	for(int i=0;i<N;i++)
	{
		int x=0,c='0';
		scanf(" ");
		getchar();
		getchar();
		for(int j=0;j<5;j++)
		{
			if(isdigit(c))c=getchar();
			x*=10;
			if(isdigit(c))x+=c-'0';
		}
		Q.push_back(x);
	}
	sort(Q.begin(),Q.end());
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d",&N);
		input(Q1);
		input(Q2);
		const int a2=solve2();
		const int a1=solve1();
		printf("Case #%d: %d %d\n",t,a1,a2);
	}
	return 0;
}
