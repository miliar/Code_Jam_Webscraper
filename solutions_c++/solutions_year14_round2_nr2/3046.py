#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

int main()
{

    freopen("B-small-attempt0.in","r",stdin);
    freopen("b.txt","w",stdout);
    int T,A,B,K;
    scanf("%d", &T);
    for(int i=1;i<=T;i++)
    {
        scanf("%d %d %d", &A, &B, &K);
        int R=0;
        for(int p=0;p<A;p++)
        {
            for(int q=0;q<B;q++)
            {
                int x = p&q;
                if(x<K)
                {
                    R++;
                }
            }
        }
        printf("Case #%d: %d\n",i,R);
    }
    return 0;
}
