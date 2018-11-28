#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

typedef pair<int,int> ii;

int main()
{
    freopen("cin.txt","r",stdin);
    freopen("cout.txt","w",stdout);
    int test_case, T;
    scanf("%d" , &T);
    for(test_case=1;test_case<=T;test_case++)
    {
        printf("Case #%d: " , test_case);
        int i, j;
        int N;
        scanf("%d" , &N);
        vector<int> F;
        F.assign(N+10, 0);
        for(i=1;i<=N;i++)
        {
            scanf("%d" , &F[i]);
        }
        int ret=0;
        vector<int> EndNum;
        EndNum.assign(N+10, 0);
        for(i=1;i<=N;i++)
        {
            int itmp=i;
            vector<bool> X;
            X.assign(N+10 , false);
            X[itmp]=true;
            int tmp=1;
            while(!X[F[itmp]])
            {
                itmp=F[itmp];
                X[itmp]=true;
                tmp++;
            }
            if(F[itmp]==i)
            {
                ret=max(ret,tmp);
                EndNum[itmp]=max(EndNum[itmp], tmp);
            }
            else if(F[F[itmp]]==itmp)
            {
                EndNum[itmp]=max(EndNum[itmp], tmp);
            }
        }
        int tmp=0;
        for(i=1;i<=N;i++)
        {
            if(F[F[i]]!=i)continue;
            //printf("%d %d %d\n" , i, EndNum[i],EndNum[F[i]]);
            tmp+=(EndNum[i]+EndNum[F[i]]-2);
        }
        ret=max(ret, tmp/2);


        printf("%d\n" , ret);



    }

    return 0;
}
