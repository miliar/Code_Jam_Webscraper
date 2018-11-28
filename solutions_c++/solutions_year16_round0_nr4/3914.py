#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<utility>
#include<iostream>
#include<string>
using namespace std;

int main()
{
    int T;
    int K, C, S;
    scanf("%d", &T);
        
    for(int i=1;i<T+1;++i)
    {
        scanf("%d%d%d", &K, &C, &S);
        printf("Case #%d:", i);
        for(int j=0;j<S;++j)
            printf(" %d", j+1);
        printf("\n");
    }
    return 0;
}
