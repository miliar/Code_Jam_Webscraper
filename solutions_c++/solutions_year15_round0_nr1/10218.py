#include<iostream>
#include<fstream>
#include<cstdio>

using namespace std;

int main()
{
    int t, smax, sum, i, f, temp, j;

    freopen("SO_inputsmall.in", "r", stdin);
	freopen("SO_outputsmall.out", "w", stdout);

    scanf("%d", &t);

    for(j=1; j<=t; j++)
    {
        f=0;
        scanf("%1d ", &smax);

        scanf("%1d", &sum);

        for(i=1; i<=smax; i++)
        {
            scanf("%1d", &temp);
            if(sum<i)
            {
                f=f+(i-sum);
                sum=i;
            }
            sum=sum+temp;
        }
        printf("Case #%d: %d\n", j, f);
    }


    return 0;
}
