#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

int T;
bool F[17];
int A,x;
int ans;

int main()
{
	//freopen("A.in","r",stdin);
    //freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for (int Case=1;Case<=T;Case++)
	{
		memset(F,0,sizeof F);
		scanf("%d",&A);
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++)
			{
				scanf("%d",&x);
				if (A==i) F[x]=true;
			}
		ans=0;
		scanf("%d",&A);
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++)
			{
				scanf("%d",&x);
				if (A==i && F[x])
                {
					if (ans==0) ans=x;
					else ans=-1;
                }
			}
		printf("Case #%d: ",Case);
		if (ans==0) printf("Volunteer cheated!\n");
		else if (ans==-1) printf("Bad magician!\n");
		else printf("%d\n",ans);
	}

    return 0;
}
