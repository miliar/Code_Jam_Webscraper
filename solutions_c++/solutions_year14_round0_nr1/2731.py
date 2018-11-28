#include <cstdlib>
#include <cstdio>

using namespace std;

int a[4][4];
int b[4][4];

int main()
{
	int t=0;
	scanf("%d",&t);
	int c=0;
	while ( t-- )
	{
		c++;
		int ans1;
		int ans2;
		scanf("%d",&ans1);
		for ( int i=0; i<4; ++i )
			for ( int j=0; j<4; ++j )
				scanf("%d",&a[i][j]);
		scanf("%d",&ans2);
		for ( int i=0; i<4; ++i )
			for ( int j=0; j<4; ++j )
				scanf("%d",&b[i][j]);

    /*    for ( int i=0; i<4; ++i )
        {
            for ( int j=0; j<4; ++j )
               printf("%d ",a[i][j]);
               printf("\n");
        }*/
		int k=0;
		int cou=0;
		for ( int i=0; i<4; ++i )
		{
			for ( int j=0; j<4; ++j )
			{
				if ( a[ans1-1][i]==b[ans2-1][j] )
				{
					k=a[ans1-1][i];
					cou++;
				}
			}
		}
	//	printf("ans1 is %d ;ans2 is %d ;cou is %d ;\n",ans1,ans2,cou);
		if ( cou==0 ) printf("Case #%d: Volunteer cheated!\n",c);
		if ( cou==1 ) printf("Case #%d: %d\n",c,k);
		if ( cou>1 ) printf("Case #%d: Bad magician!\n",c);
	}
	return 0;
}
