

#include <iostream>
#include <cstdio>
#include <cstring>

#define LL long long
#define ULL unsigned long long
using namespace std;
int main() {
    
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; i++)
    {
        LL n;
        scanf("%lld",&n);
        if(n == 0)
        {    printf("Case #%d: INSOMNIA\n",i);
        }
        else if (n == 1)
        {    printf("Case #%d: 10\n",i);
        }
        else
        {
            LL pointer = 1;
            int arr[10],count = 0;
            for(int i = 0 ; i < 10 ; i++)
            {   arr[i] = 0;
            }
            while (count != 10)
            {
                LL tmp = n*pointer;
                while(tmp != 0)
                {
                    LL val = tmp%10;
                    if (arr[val] == 0) {
                        count += 1;
                        arr[val] = 1;
                    }
                    tmp = tmp/10;
                }
                pointer++;
            }
            printf("Case #%d: %lld\n",i,n*(pointer-1));
        }
    }
    return 0;
}

