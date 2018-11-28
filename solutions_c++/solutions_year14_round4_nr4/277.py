#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;

int M, N, ans1, ans2, top[15];
string S[15], T[15][15], R[15];

void Dfs(int x)
{
	if (x>M)
	{
		int cur(0);
		for (int i=1;i<=N;i++)
		{
			if (!top[i]) return;
			for (int j=1;j<=top[i];j++) R[j]=T[i][j];
			sort(R+1,R+top[i]+1);
			for (int j=1;j<=top[i];j++) cur+=R[j].length();
			for (int j=2;j<=top[i];j++)
			{
				size_t k(0);
				while (k<R[j].length() && k<R[j-1].length() && R[j][k]==R[j-1][k]) k++;
				cur-=k;
			}
		}
		if (cur>ans1)
			ans1=cur, ans2=0;
		if (cur==ans1)
			ans2++;
		return;
	}
	for (int i=1;i<=N;i++)
	{
		T[i][++top[i]]=S[x];
		Dfs(x+1);
		T[i][top[i]--]="";
	}
}

int main()
{
	freopen("p4.in","r",stdin);
	freopen("p4.out","w",stdout);
	int TT;
	scanf("%d",&TT);
	for (int tt=1;tt<=TT;tt++)
	{
		ans1=ans2=0;
		scanf("%d%d",&M,&N);
		for (int i=1;i<=M;i++) cin>>S[i];
		Dfs(1);
		printf("Case #%d: %d %d\n",tt,ans1+N,ans2);
	}
	return 0;
}

