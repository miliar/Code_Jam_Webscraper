#include <iostream>
#include <cstdio>

#define sz 1005
using namespace std;

int A[sz];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int iterator=1;iterator<=T;iterator++)
    {
        int N;
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            scanf("%d",&A[i]);
        }

        int max_diff=0;
        int answer=0;
        for(int i=1;i<N;i++)
        {
            if(A[i]<A[i-1])
            {
                answer+=A[i-1]-A[i];
            }
            if(max_diff<A[i-1]-A[i])
            {
                max_diff=A[i-1]-A[i];
            }
        }

        int z=0;
        for(int i=0;i<N-1;i++)
        {
            z+=min(max_diff,A[i]);
        }

        printf("Case #%d: %d %d\n",iterator,answer,z);

    }
}
