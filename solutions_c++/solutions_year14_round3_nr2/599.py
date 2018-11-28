#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

char s[1010][110];
int typ[1010];
int T,n;

void lable(int num, char ss[])
{
	int l=strlen(ss);
	if (l==1) {typ[num]=1; return;}
	if (l==2)
	{
		if (ss[0]==ss[1]) typ[num]=2;
		else typ[num]=3; 
		return;
	}
	int p=ss[0],change=0,key=4;
	for (int i=0;i<l;i++)
	{
		if (ss[i]==p) continue;
		else
		{
			if (change==1) {typ[num]=5; return;}
			p=ss[l-1]; change=1;
		}
	}
	typ[num]=4; return;
}

int flag[30];
int checkneibug(int i,int len)
{
	memset(flag,0,sizeof flag);
	char prej=s[i][0];
	for (int j=0;j<len;j++)
	{
		if (s[i][j]==prej) { continue; }
		if (flag[prej-'a']==1) return 1;
		flag[prej-'a']=1;
		prej=s[i][j]; 
	}
	if (flag[s[i][len-1]-'a']) return 1;
	else return 0;
}

int main()
{
	/*
	while (cin>>s[1]) 
	{
		printf("%d\n", checkneibug(1,strlen(s[1]))); 
	}
	return 0;
	*/
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++)
	{
		int ans=-1;
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
			scanf("%s",s[i]);
		memset(typ,0,sizeof typ);

		for (int i=1;i<=n;i++)
		{
			int l=strlen(s[i]);
			lable(i,s[i]);
			if (typ[i]==4) 
			{
				s[i][1]=s[i][l-1];
				s[i][2]=s[i][l];
				typ[i]=3;
			}
			if (typ[i]==5)
			{
				if (checkneibug(i,l)==1) {ans=0; break;}
			}
		}

		if (ans!=-1) { printf("Case #%d: 0\n",TT); continue;}

		
	}
	return 0;
}