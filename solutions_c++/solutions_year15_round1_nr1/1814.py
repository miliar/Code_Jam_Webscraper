#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output2.txt","w",stdout);
    int n,N;
    int mush[1100];
    scanf("%d",&N);
    for(int T=1;T<=N;T++){
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d",&mush[i]);
        int c1=0,c2=0,k=0;
        for(int i=0;i<n-1;i++){
            int j=mush[i]-mush[i+1];
            if(j>0){
                c1+=j;
                if(j>k)
                    k=j;
            }
        }
        for(int i=0;i<n-1;i++){
            if(mush[i]<k)
                c2+=mush[i];
            else
                c2+=k;
        }
        printf("Case #%d: %d %d\n",T,c1,c2);
    }
    return 0;
}
