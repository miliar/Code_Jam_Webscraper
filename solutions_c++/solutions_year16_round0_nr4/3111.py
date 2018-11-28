#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <map>
using namespace std;

int k,c,s;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    //freopen("B-large.in","r",stdin);
    freopen("a.txt","w",stdout);
    scanf("%d", &T);
	for (int cse = 1; cse <= T; cse++)
	{
        scanf("%d %d %d", &k, &c, &s);

        printf("Case #%d:",cse);
        for (int i = 1; i <= k; i++)
            printf(" %d", i);
        printf("\n");
	}
	return 0;
}
