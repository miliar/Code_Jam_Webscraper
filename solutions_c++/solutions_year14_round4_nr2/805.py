#include<cstdio>
#include<algorithm>

int s[1100],_s[1100],n,Ans,TestCase,Case;

bool cmp(int a,int b){return s[a]<s[b];}

void Swap(int i,int j)
{
	int k(s[i]);
	s[i]=s[j];
	s[j]=k;
	_s[s[i]]=i;
	_s[s[j]]=j;
	Ans++;
}

int main()
{
	int i,j,L,R;
//	freopen("b.in","rb",stdin);
//	freopen("b.out","wb",stdout);
	scanf("%d",&TestCase);
	for(Case=1;Case<=TestCase;Case++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)scanf("%d",s+i);
		for(i=0;i<n;i++)_s[i]=i;
		std::sort(_s,_s+n,cmp);
		for(i=0;i<n;i++)s[_s[i]]=i;
		Ans=0;
		for(L=i=0,R=n-1;i<n;i++)
		{
			if((_s[i]-L)<(R-_s[i]))
			{
				for(;_s[i]!=L;Swap(_s[i],_s[i]-1));
				L++;
			}
			else
			{
				for(;_s[i]!=R;Swap(_s[i],_s[i]+1));
				R--;
			}
		}
		printf("Case #%d: %d\n",Case,Ans);
	}
	return 0;
}
