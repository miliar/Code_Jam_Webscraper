//
//  main.cpp
//  cj14_round0_a
//

#include <iostream>
#include <cstdio>

int main()
{
    int T, TN, i, j, c[16], a, n[4], count, num;
    freopen("A-small.in","r",stdin);
    freopen("A-small.txt","w",stdout);
    scanf("%d", &TN);
    for (T = 0; T<TN; T++)
    {
	memset(c, 0, sizeof(int)*16);
	scanf("%d", &a);
        for (i = 1; i<=4; i++)
	{
		scanf("%d%d%d%d",n,n+1,n+2,n+3);
		if (i==a)
            	{	for (j = 0; j<4; j++)
				c[n[j]-1]=1;
            	}
	}
	count = 0;
	scanf("%d",&a);
	for (i = 1; i<=4;i++)
	{
		scanf("%d%d%d%d",n,n+1,n+2,n+3);
		if (i==a)
			for (j=0; j<4; j++){
				count += c[n[j]-1];
				if (c[n[j]-1]==1)
					num = n[j];
			}
	}
        printf("Case #%d: ", T+1);
        switch (count)
        {
            case (1):
                    printf("%d\n", num);break;
	    case (3): case(4):
            case (2): printf("Bad magician!\n"); break;
            case (0): printf("Volunteer cheated!\n");
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}


