#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int N, Smax;
char s[1010];
int main()
{
	freopen ("data.in", "r",stdin);
	freopen ("data.out","w",stdout);
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        int rst = 0;
        int sum = 0;
        scanf("%d", &Smax);
        scanf("%s", s);
        for (int j = 0; j < Smax+1; j++)
        {
            s[j] -= '0';
        }
        for(int j = 0; j < Smax+1; j++)
        {
            if(sum>=j) sum += s[j];
            else
                {
                    rst = rst+j-sum;
                    sum = j+s[j];
                }
        }
        printf("Case #%d: %d\n", i+1,rst);
    }


	return 0;
}
