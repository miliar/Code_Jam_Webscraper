#include <cstdio>

using namespace std;

int main()
{
    int N,a,b,c,t,ans,i,j;
    scanf("%d",&N);
    for(t=1;t<=N;t++){
        ans=0;
        scanf("%d %d %d",&a,&b,&c);
        for(i=0;i<a;i++){
            for(j=0;j<b;j++){
                if((i&j)<c)ans++;
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
