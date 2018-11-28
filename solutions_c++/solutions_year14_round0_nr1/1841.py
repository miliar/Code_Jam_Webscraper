#include <stdio.h>

int tc;
int a,r[22][2],s[2];
int t,w;

int main()
{
	int o,i,j,k;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	for(scanf("%d",&tc),o=1;o<=tc;++o)
	{
		for(k=0;k<=1;++k)
		{
			scanf("%d",&s[k]);
			for(i=1;i<=4;++i)
				for(j=1;j<=4;++j)
					scanf("%d",&a),r[a][k]=i;
		}
		t=0;
		for(i=1;i<=16;++i)
			if(r[i][0]==s[0] && r[i][1]==s[1])
				++t,w=i;
		printf("Case #%d: ",o);
		if(t==0) printf("Volunteer cheated!\n");
		else if(t>1) printf("Bad magician!\n");
		else printf("%d\n",w);			
	}
	return 0;
}