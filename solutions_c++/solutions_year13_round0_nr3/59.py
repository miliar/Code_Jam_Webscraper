#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <numeric>
#include <cstring>

typedef long long i64d;

using namespace std;

char ans[45000][110];

void mul(char c[], char a[], char b[])
{
	int	i,j,len;
	memset(c,0,sizeof(c));
	for( i=1;i<=a[0];++i )
		for( j=1;j<=b[0];++j )
		{
			c[i+j-1]	+=	a[i]*b[j];
			c[i+j]		+=	c[i+j-1]/10;
			c[i+j-1]	=	c[i+j-1]%10;
		}
	len=a[0]+b[0]+1;
	while( len>1 && c[len]==0 ) len--;
	c[0]=len;
}

int cmp(char a[] , char b[])
{
    if (a[0] > b[0]) return 1;
    else if (a[0] < b[0]) return -1;
    else
    {
        for (int i = 1; i <= a[0]; i ++)
            if (a[i] > b[i]) return 1;
            else if (a[i] < b[i]) return -1;
    }
    return 0;
}

int main()
{
	freopen("C-large-2.in" , "r" , stdin);
	//freopen("input.txt" , "r" , stdin);
	freopen("C-large-2.out" , "w" , stdout);
	int cas;
	scanf("%d" , &cas);

    int sum = 3;
    ans[0][0] = 1; ans[0][1] = 1;
    ans[1][0] = 1; ans[1][1] = 4;
    ans[2][0] = 1; ans[2][1] = 9;
    for (int i = 3; i <= 100; i += 2)
    {
        int x = (i+1)/2;
        int y = x / 2;
        char a[55],b[55] , ab[101];
        a[0] = x; 
        for (int j = 0; j <= 3; j ++)
        if (j <= y-1)
        {
            char half[26] = "";
            for (int k = 0;k < j; k ++) half[y-2-k] = 1;
            do
            {
                a[1] = 1;
                for (int t = 0; t < y-1; t ++) a[t+2] = half[t];
                if (x & 1)
                {
                    a[y+1] = 0;
                    int po = y+2;
                    for (int t = y; t >= 1; t --) a[po++] = a[t];
                    memcpy(b , a , x+1);
                    mul((char*)ans[sum++] , a , b);

                    a[y+1] = 1;
                    po = y+2;
                    for (int t = y; t >= 1; t --) a[po++] = a[t];
                    memcpy(b , a , x+1);
                    mul((char*)ans[sum++] , a , b);

                    if (j < 2)
                    {
                        a[y+1] = 2;
                        po = y+2;
                        for (int t = y; t >= 1; t --) a[po++] = a[t];
                        memcpy(b , a , x+1);
                        mul((char*)ans[sum++] , a , b);
                    }
                }
                else
                {
                    int po = y+1;
                    for (int t = y; t >= 1; t --) a[po++] = a[t];
                    memcpy(b , a , x+1);
                    mul((char*)ans[sum++] , a , b);
                }
            }
            while (next_permutation(half , half+y-1));
        }
        //2000..0002
        a[1] = 2; a[x] = 2; b[1] = 2; b[x] = 2;
        for (int t = 2; t < x; t ++) {a[t] = 0; b[t] = 0;}
        mul((char*)ans[sum++] , a , b);

        if (x & 1)
        {
            a[y+1] = 1; b[y+1] = 1;
            mul((char*)ans[sum++] , a , b);
        }
    }
    /*
    for (int i = 0; i < sum; i ++)
    {
        for (int j = 1; j <= ans[i][0]; j ++)
            printf("%d" , (int)ans[i][j]);
        printf("\n");
    }
    */
    
	for (int ca = 1; ca <= cas; ca ++)
	{
		printf("Case #%d: " , ca);
        char A[110] , B[110] , a[110] , b[110];
        scanf("%s %s" , A , B);
        a[0] = strlen(A);
        for (int i = 0; i < a[0]; i ++) a[i+1] = A[i]-'0';
        b[0] = strlen(B);
        for (int i = 0; i < b[0]; i ++) b[i+1] = B[i]-'0';
        int res = 0;
        for (int i = 0; i < sum; i ++)
            if (cmp((char*)ans[i] , a) >= 0 && cmp((char*)ans[i] , b) <= 0) res ++;
        printf("%d\n" , res);
    }
    return 0;
}