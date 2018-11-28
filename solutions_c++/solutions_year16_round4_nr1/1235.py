#include <stdio.h>
#include <string>
void solve(int);
int main()
{
	freopen("AinputL.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++) solve(i);
}
char A[5] = {'-','P','R','S'};
int ans[5][10010];
int num[5][5];
int a,b,c,d,C=1;
std::string func(int s, int t, int k)
{
	if(s>C)
	{
		num[k][t]++;
		if(t==1) return "1";
		if(t==2) return "2";
		if(t==3) return "3";
	}
	if(t==1)
	{
		std::string s1 = func(2*s,1,k);
		std::string s2 = func(2*s+1,2,k);
		if(s1<s2) return s1+s2;
		else return s2+s1;
	}
	if(t==2)
	{
		std::string s1 = func(2*s,2,k);
		std::string s2 = func(2*s+1,3,k);
		if(s1<s2) return s1+s2;
		else return s2+s1;
	}
	if(t==3)
	{
		std::string s1 = func(2*s,1,k);
		std::string s2 = func(2*s+1,3,k);
		if(s1<s2) return s1+s2;
		else return s2+s1;
	}
}
void print(int k, int s, int t)
{
	int i;
	if(num[k][1]==c&&num[k][2]==b&&num[k][3]==d)
	{
		for(i=1;i<=(1<<a);i++) printf("%c",A[ans[k][i]]);
		return;
	}
	else if(num[s][1]==c&&num[s][2]==b&&num[s][3]==d)
	{
		for(i=1;i<=(1<<a);i++) printf("%c",A[ans[s][i]]);
		return;
	}
	else if(num[t][1]==c&&num[t][2]==b&&num[t][3]==d)
	{
		for(i=1;i<=(1<<a);i++) printf("%c",A[ans[t][i]]);
		return;
	}
	else printf("IMPOSSIBLE");
}
void solve(int T)
{
	//1 = paper, 2 = rock, 3 = scissor
	int count1=0,count2=0,count3=0,i,j;
	scanf("%d%d%d%d",&a,&b,&c,&d);
	C = (1<<a)-1;
	for(i=1;i<=3;i++) for(j=1;j<=3;j++) num[i][j]=0;
	for(j=1;j<=3;j++)
	{
		std::string S = func(1,j,j);
		for(i=1;i<=(1<<a);i++)
		{
			ans[j][i] = S[i-1] - '1' + 1;
		}
	}
	for(i=1;i<=(1<<a);i++)
	{
		if(ans[1][i]<ans[2][i])
		{
			count1++;
			break;
		}
		if(ans[1][i]>ans[2][i])
		{
			count2++;
			break;
		}
	}
	for(i=1;i<=(1<<a);i++)
	{
		if(ans[1][i]<ans[3][i])
		{
			count1++;
			break;
		}
		if(ans[1][i]>ans[3][i])
		{
			count3++;
			break;
		}
	}
	for(i=1;i<=(1<<a);i++)
	{
		if(ans[3][i]<ans[2][i])
		{
			count3++;
			break;
		}
		if(ans[3][i]>ans[2][i])
		{
			count2++;
			break;
		}
	}
	printf("Case #%d: ",T);
	if(count1==2&&count2==1&&count3==0) print(1,2,3);
	if(count1==2&&count2==0&&count3==1) print(1,3,2);
	if(count1==1&&count2==2&&count3==0) print(2,1,3);
	if(count1==1&&count2==0&&count3==2) print(3,1,2);
	if(count1==0&&count2==2&&count3==1) print(2,3,1);
	if(count1==0&&count2==1&&count3==2) print(3,2,1);
	printf("\n");
}
