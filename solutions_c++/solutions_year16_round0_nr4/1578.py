#include <bits/stdc++.h>

using namespace std;

int test , T , K , C , S , i;

int main()
{
freopen("test.in" , "r" , stdin);
freopen("test.out" , "w" , stdout);

scanf("%d" , &T);
for (test = 1 ; test <= T ; ++test)
{
    scanf("%d" , &K);
    scanf("%d" , &C);
    scanf("%d" , &S);

    printf("Case #%d: " , test);
    for (i = 1 ; i <= K ; ++i)
    printf("%d " , i);

    printf("\n");
}

return 0;
}
