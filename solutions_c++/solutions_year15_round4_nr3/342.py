#include<cstdio>
#include<vector>
#include<algorithm>

char s[22222];

std::vector<long long> a[22];
long long d[2222];
int dn;

int p[2222][2];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    int tc,tcn;
    scanf("%d\n",&tcn);
    for(tc=1;tc<=tcn;tc++)
	{
		long long t;
		int i,j,k,n;
		int min,now;
		scanf("%d\n",&n);
		dn=0;
		for(i=0;i<n;i++)
		{
			a[i].clear();
			fgets(s,20155,stdin);
			t=0;
			for(j=0;s[j];j++)
			{
				if(s[j]==' '||s[j]=='\n')
				{
					a[i].push_back(t);
                    d[dn++]=t;
                    t=0;
				}
				else t=t*27+s[j]-'a'+1;
			}
		}
		std::sort(d,d+dn);
        for(i=0;i<n;i++)for(j=0;j<a[i].size();j++)a[i][j]=std::lower_bound(d,d+dn,a[i][j])-d;
        min=1e9;
        for(i=2;i<(1<<n);i+=4)
		{
			for(j=0;j<dn;j++)p[j][0]=p[j][1]=0;
            for(j=0;j<n;j++)for(k=0;k<a[j].size();k++)p[a[j][k]][(i>>j)&1]=1;
            now=0;
            for(j=0;j<dn;j++)if(p[j][0]&&p[j][1])now++;
            min=std::min(min,now);
		}
		printf("Case #%d: %d\n",tc,min);
	}
}
