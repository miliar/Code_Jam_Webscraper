/*
* Filename:    B.cpp
* Desciption:  B
* Created:     2016年04月09日 14时16分47秒 星期六
* Author:      JIngwei Xu [mail:xu_jingwei@outlook.com]
*
*/
#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<vector>
using namespace std;
typedef pair<int,int> P;
typedef long long ll;

//Init Const
const int INF=1e9;
const int maxn=1000+7;

//Global Variables
int n,m,t,ans;
char s[107];
int a[107];
//Function Declaration
int solve(int num,int flip);

//Main Program
int main()
{
#ifdef AC_THIS_PROBLEM
	freopen("B-large.in","r",stdin);
	freopen("data.out","w",stdout);
#endif
	//Init
	
	
	
	//Input
	scanf("%d",&t);
	for (int caset = 1; caset <=t; caset += 1)
	{
		scanf("%s",s);
		for (int i = 0; i < 107; i += 1)
		{
			if(s[i]=='+')a[i]=1;
			else if(s[i]=='-')a[i]=0;
			else {n=i;break;}
		}
		//printf("%d\n",n);
		ans=solve(n,1);
		printf("Case #%d: %d\n",caset,ans);
	}
	return 0;
}
int solve(int num,int flip){
	if(num==1)return flip!=a[0];
	int pos1=0,pos2=0;
	for (int i = num; i >=1; i += -1){
		if(a[i-1]==flip)continue;
		pos1=i;break;
	}
	if(pos1==0)return 0;
	for (int i = pos1; i >=1; i += -1)
	{
		if(a[i-1]!=flip)continue;
		pos2=i;break;
	}
	if(pos2==0)return 1;
	return solve(pos2,1-flip)+1;
	
}
