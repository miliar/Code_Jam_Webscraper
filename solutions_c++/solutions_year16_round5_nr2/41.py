#include <bits/stdc++.h>
using namespace std;
int Test,N,s1,s2,pt,last,len,M;
char sch[110],s[110],q[110];
int sett[110],fail[110],size[110];
int st[110],ne[110],go[110],fa[110];
void Add(int x,int y){ne[++pt]=st[x];st[x]=pt;go[pt]=y;}
void deal(){
	last=0;
	for (int i=st[0];i;i=ne[i])sett[++last]=go[i];
	int r=0;
	for (int step=1;step<=N;step++){
		int sum=0;
		for (int i=1;i<=last;i++)sum+=size[sett[i]];
		int x=rand()%sum+1;
		for (int i=1;i<=last;i++)
			if (x>size[sett[i]])x-=size[sett[i]];
			else{
				x=i;
				break;
			}
		int y=sett[x];
		q[++r]=sch[y];
		sett[x]=sett[last];
		sett[last--]=0;
		for (int i=st[y];i;i=ne[i])
			sett[++last]=go[i];
	}
}
void buildfail(){
	len=strlen(s+1);
	fail[1]=0;
	for (int i=2;i<=len;i++){
		int x=fail[i-1];
		while (x&&s[i]!=s[x+1])
			x=fail[x];
		if (s[i]==s[x+1])fail[i]=x+1;
		else fail[i]=0;
	}
}
bool check(){
	int x=0;
	for (int i=1;i<=N;i++){
		while (x&&q[i]!=s[x+1])x=fail[x];
		if (q[i]==s[x+1])x++;
		else x=0;
		if (x==len)return 1;
	}
	return 0;
}
void dfs(int x){
	size[x]=1;
	for (int i=st[x];i;i=ne[i]){
		dfs(go[i]);
		size[x]+=size[go[i]];
	}
}
int main(){
	srand(time(0));
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&Test);
	for (int tt=1;tt<=Test;tt++){
		printf("Case #%d:",tt);
		scanf("%d",&N);
		memset(fa,0,sizeof(fa));
		memset(st,0,sizeof(st));
		memset(size,0,sizeof(size));
		pt=0;
		for (int i=1;i<=N;i++)
			scanf("%d",&fa[i]),Add(fa[i],i);
		dfs(0);
		scanf("%s",sch+1);
		scanf("%d",&M);
		for (int i=1;i<=M;i++){
			scanf("%s",s+1);
			buildfail();
			s1=s2=0;
			for (int step=1;step<=20000;step++){
				s2++;
				deal();
				if (check())s1++;
			}
			printf(" %.2lf",double(s1)/s2);
		}
		printf("\n");
	}
}