#include<stdio.h>
#include<memory.h>
#include<string.h>
FILE*in=fopen("input.txt","r");
FILE*out=fopen("output.txt","w");
long long A,B;
char buf1[101],buf2[101];
char a[101],b[101];
char c[101];
int LA,LB;
int cnt;
int flag;
char buf[101];
void dfs(int N,int x,int y,int S)
{
	if(x>y)
	{
		int i,j,k;
		int carry=0,g;
		for(k=100;k>=0;k--)
		{
			g=carry; carry=0;
			for(i=100;i>=k;i--)
			{
				j=k-i+100;
				if(j<0||j>100) continue;
				g+=(buf[i]-'0')*(buf[j]-'0');
			}
			c[k]=(g%10)+'0';
			carry=g/10;
		}
		for(i=0;i<=100;i++)
		{
			if(c[i]>b[i])
			{
				flag=1;
				return;
			}
			if(c[i]<b[i]) break;
		}
		for(i=0;i<=100;i++)
		{
			if(a[i]<c[i]) break;
			if(a[i]>c[i]) return;
		}
		for(i=0;i<=100;i++) if(c[i]!='0') break;
		for(j=100;i<=j;i++,j--)
		{
			if(c[i]!=c[j]) return;
		}
		cnt++;
		//fprintf(out,"%s %s\n",&buf[100-N+1],c);
		return;
	}
	int i;
	for(i=0;i<3;i++)
	{
		if(x==100-N+1&&i==0) continue;
		if(x==y)
		{
			if(S+i>10) continue;
			buf[x]=i+'0';
			dfs(N,x+1,y-1,S+i);
			buf[x]='0';
		}
		else
		{
			if(S+2*i>10) continue;
			buf[x]=buf[y]=i+'0';
			dfs(N,x+1,y-1,S+2*i);
			buf[x]=buf[y]='0';
		}
	}
}
int main()
{
	int T,t;
	fscanf(in,"%d",&T);
	int i,j;
	for(t=1;t<=T;t++)
	{
		cnt=flag=0;
		fscanf(in,"%s %s",buf1,buf2);
		LA=strlen(buf1);
		LB=strlen(buf2);
		if(LA==1)
		{
			if(LB==1)
			{
				if(buf1[0]<='1'&&'1'<=buf2[0]) cnt++;
				if(buf1[0]<='4'&&'4'<=buf2[0]) cnt++;
				if(buf1[0]<='9'&&'9'<=buf2[0]) cnt++;
			}
			else
			{
				if(buf1[0]<='1') cnt++;
				if(buf1[0]<='4') cnt++;
				if(buf1[0]<='9') cnt++;
			}
		}
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(i=100,j=LA-1;i>=0&&j>=0;i--,j--) a[i]=buf1[j];
		for(i=100,j=LB-1;i>=0&&j>=0;i--,j--) b[i]=buf2[j];
		for(i=0;i<=100;i++)
		{
			if(a[i]==0) a[i]='0';
			if(b[i]==0) b[i]='0';
			buf[i]='0';
		}
		for(i=2;i<=LB;i++)
		{
			if(i==1) continue;
			dfs(i,100-i+1,100,0);
			if(flag) break;
		}
		fprintf(out,"Case #%d: %d\n",t,cnt);
	}
}