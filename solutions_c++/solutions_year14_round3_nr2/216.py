#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int l[105],r[105],ok,cts,n;
bool a[105][30],mi[30],cd[105];
char c[105][105];
int all[30],lc[30],rc[30];
const int mod=1000000007;
long long tot;

long long fnd(int x)
{
	long long s=1;
	int i;
	if(all[x])
		for(i=1;i<=all[x];i++)
			s=s*i%mod;
	all[x]=0;
	for(i=0;i<n;i++)
		if(!cd[i]&&l[i]==x)
		{
			cd[i]=1;
			ok++;
			s=s*fnd(r[i])%mod;
		}
	return s;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t,i,j,len,lst;
	long long t2;
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		memset(a,0,sizeof(a));
		memset(mi,0,sizeof(mi));
		memset(all,0,sizeof(all));
		memset(cd,0,sizeof(cd));
		memset(lc,0,sizeof(lc));
		memset(rc,0,sizeof(rc));
		ok=cts=0;
		tot=1;
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%s",c[i]);
		printf("Case #%d: ",t);
		for(i=0;i<n;i++)
		{
			len=strlen(c[i]);
			l[i]=c[i][0]-'a',r[i]=c[i][len-1]-'a';
			for(lst=j=0;j<len;j++)
			{
				if(c[i][j]!=lst)
				{
					lst=c[i][j]-'a';
					if(l[i]==r[i]&&lst!=l[i])
						break;
					if(a[i][lst])
						break;
					if(lst!=l[i]&&lst!=r[i]&&mi[lst])
						break;
					a[i][lst]=1;
					mi[lst]=1;
					lst+='a';
				}
			}
			if(j<len)
				break;
			if(l[i]==r[i])
				all[l[i]]++,cd[i]=1,ok++;
			else
			{
				lc[l[i]]++,rc[r[i]]++;
				if(lc[l[i]]>1||rc[r[i]]>1)
					break;
			}
		}
		if(i<n)
		{
			puts("0");
			continue;
		}
		for(i=0;i<26;i++)
			if(lc[i]&&!rc[i])
				if(t2=fnd(i))
					tot=tot*t2%mod,cts++;
				else
					break;
		for(i=0;i<26;i++)
			if(all[i])
			{
				for(t2=1,j=1;j<=all[i];j++)
					tot=tot*j%mod;
				cts++;
			}
		if(ok<n)
		{
			puts("0");
			continue;
		}
		for(i=1;i<=cts;i++)
			tot=tot*i%mod;
		printf("%I64d\n",tot);
	}
	return 0;
}
