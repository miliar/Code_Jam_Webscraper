#include <cstdio>
#include <cstdlib>
using namespace std;
int main()
{

    int T,nm,N,n[26],sum,step[1004],ava[1005];
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        scanf("%d",&nm);
        sum=0;
        for(int j=0;j<nm;j++)
        {
            scanf("%d",&n[j]);
            sum+=n[j];
        }
        int t=sum;
        printf("Case #%d:",i+1);
        while(t>0)
        {
            int id=-1;
            for(int j=0;j<nm;j++)
            {
                if(id==-1 || n[id]<n[j])id=j;
            }
//            if(t!=1)printf(" ");

//            printf("%d\n",n[id]);
            if(n[id]>t/2) ava[sum-t]=0;
            else ava[sum-t]=1;
            if(ava[sum-t]!=0)printf(" ");
            printf("%c",id+'A');
            n[id]--;

            t--;

        }
        printf("\n");
    }
    return 0;
}
