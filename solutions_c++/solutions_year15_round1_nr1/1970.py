#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int N, Smax;
int data[1010];
int main()
{
	freopen ("data.in", "r",stdin);
	freopen ("data.out","w",stdout);
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        int rst1 = 0;
        int rst2 = 0;
        int flag = 0;
        scanf("%d", &Smax);
        for(int j = 0; j < Smax; j++)
        {
            scanf("%d", &data[j]);
            flag = flag+1;
        }
        int t_max = 0;
        for(int j = 0; j+1 < Smax; j ++)
        {
            int temp = data[j]-data[j+1];
            int temp1 = temp > 0 ? temp : 0;
            rst1 = rst1+temp1;
            if(temp>t_max) t_max = temp;
        }
        for(int j = 0; j+1 < Smax; j ++)
        {

            int temp2 = data[j] > t_max ? t_max : data[j];
            rst2 = rst2+temp2;
        }

        printf("Case #%d: %d %d\n", i+1, rst1, rst2);
    }

	return 0;
}
