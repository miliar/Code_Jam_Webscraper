#include <bits/stdc++.h>

#define pi acos(-1)
#define mod 1000000007
typedef long long ll;

using namespace std;

int main()
{
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int n;
	char a[1010], b[1010];
	scanf("%d", &n);
	getchar();
	for(int i=1; i<=n; i++)
    {
        scanf("%s", a);
        int x = strlen(a), p=1, q, j;
        b[0] = a[0];
        char ch = a[0];
        for(j=1; j<x; j++)
        {
            if(a[j]>=ch)
            {
                ch = a[j];
                for(int k=j+1; k>=1; k--)
                {
                    b[k] = b[k-1];
                }
                b[0] = ch;
            }
            else
            {
                b[j] = a[j];
            }
        }
        b[x] = 0;
        printf("Case #%d: %s\n",i, b);
    }
	return 0;
}
