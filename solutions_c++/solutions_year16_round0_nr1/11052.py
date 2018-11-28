#include<bits/stdc++.h>
using namespace std;

int main()
{
   unsigned long long int flag[10], i, j, k, l, n, m;
   int test, cno = 0;
    //freopen("i.txt", "rt", stdin);
    //freopen("output.txt", "w", stdout);
   scanf("%d", &test);

   while(test--){
    memset(flag, 0, sizeof(flag));

    scanf("%llu", &n);
    if(n == 0)
        printf("Case #%d: INSOMNIA\n", ++cno);
    else
    for(i = 1; ;i++){
        k = i * n;
        while(k != 0){
            l = k % 10;
            flag[l] = 1;
            k = k / 10;
        }

        for(j = 0; j < 10; j++){
            if(flag[j] == 0)
                break;
        }

        if(j == 10)
        {
            printf("Case #%d: %llu\n",++cno, n * i);
            break;
        }
    }

   }
   return 0;

}
