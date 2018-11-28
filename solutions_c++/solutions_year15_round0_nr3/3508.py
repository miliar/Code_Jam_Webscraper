#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int N, len, times;
char s[6] = "xyijk";
char in[20020];
char temp[20020];
int length;
int table[5][5] = {{0,1,2,3,4},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int getint(char s)
{
    switch (s)
    {
        case 'i': return 2;
        case 'j': return 3;
        case 'k': return 4;
        default: return 0;
    }
}
int main()
{
	freopen ("data.in", "r",stdin);
	freopen ("data.out","w",stdout);
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d %d", &len, &times);
        scanf("%s", temp);
        length = len*times;
        for(int j = 0; j < length; j++)
        {
            in[j] = temp[ j%len];
        }
        int flag = 0;
        int rst = 0;
        int sucess  = 0;
        int sign  = 1;
        for(int j = 0, cmp = 2; j < length; j++)
        {
            if (rst<0) {sign = -1; rst  = -rst;}
             else sign = 1;
            in[j] = getint(in[j]);
            rst = sign * table[rst][in[j]];
            if(rst == cmp)
            {
                cmp++;
                rst = 0;
                flag = j;
            }
            if (cmp == 4)
            {
                rst = 0;
                for (j = flag; j<length; j++)
                 {
                    if (rst<0) {sign = -1; rst  = -rst;}
                    else sign = 1;
                    in[j] = getint(in[j]);
                    rst = sign * table[rst][in[j]];
                 }
                if(rst == 4) sucess = 1;
                else sucess = 0;
            }
        }

        if(sucess) printf("Case #%d: YES\n", i+1);
        else printf("Case #%d: NO\n", i+1);
    }


	return 0;
}
