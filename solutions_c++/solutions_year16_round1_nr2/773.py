#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main()
{
    freopen("bin.txt","r",stdin);
    freopen("bout.txt","w",stdout);
    int test_case, T;
    scanf("%d" , &T);
    for(test_case=1;test_case<=T;test_case++)
    {
        printf("Case #%d: " , test_case);
        int i, j;
        vector<bool> X;
        X.assign(2510, false);
        int N;
        int tmp;
        scanf("%d" , &N);
        for(i=0;i<N*(2*N-1);i++)
        {
            scanf("%d" , &tmp);
            X[tmp]=!X[tmp];
        }
        int checking=0;
        for(i=1;i<=2500;i++)
        {
            if(X[i])
            {
                printf("%d " , i);
                checking++;
            }
        }
        printf("\n");
        if(checking!=N)
        {
            printf("Not Good\n");
        }


    }

    return 0;
}
