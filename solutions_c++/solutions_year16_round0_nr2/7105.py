#include<bits/stdc++.h>

using namespace std;


int main()
{
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int tc, i, j;
	scanf("%d", &tc);
	for(i=1; i<=tc; i++)
    {
        int cnt=0;
        char a[110];
        scanf("%s", a);
        int x = strlen(a);
        if(x==1 && a[0]=='-')
            cnt++;
        else
        {
            for(j=0; j<x-1; j++)
            {
                if(a[j] != a[j+1])
                {
                    cnt++;
                }
            }
            if(a[x-1]=='-')cnt++;
        }
        printf("Case #%d: %d\n",i, cnt);
    }
    return 0;
}
