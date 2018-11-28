#include<cstdio>
#include<algorithm>

int s[11000],n,X,Cnt,TestCase,Case;

int main()
{
	int i,j;
//	freopen("a.in","rb",stdin);
//	freopen("a.out","wb",stdout);
	scanf("%d",&TestCase);
	for(Case=1;Case<=TestCase;Case++)
	{
		scanf("%d%d",&n,&X);
		for(i=0;i<n;i++)scanf("%d",s+i);
		std::sort(s,s+n);
		Cnt=0;
		for(i=n-1,j=0;i>=j;i--)
		{
			if(i==j)Cnt++;
			else if(s[i]+s[j]<=X)
			{
				j++;
				Cnt++;
			}
			else Cnt++;
		}
		printf("Case #%d: %d\n",Case,Cnt);
	}
	return 0;
}
