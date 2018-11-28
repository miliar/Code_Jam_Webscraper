#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int maxn=1005;

int m[maxn];
int N;
int s0,mid,s1;

int main()
{
    int T;
    //freopen("A-large.in","r",stdin);
    //freopen("output1.out","w",stdout);
    scanf("%d",&T);
    for(int kk=1;kk<=T;kk++){
        scanf("%d",&N);
        s0=s1=mid=0;
        for(int i=0;i<N;i++) scanf("%d",&m[i]);
        for(int i=0;i<N-1;i++){
            if(m[i]>m[i+1]) s0+=m[i]-m[i+1];
            mid=max(mid,m[i]-m[i+1]);
        }
        for(int i=0;i<N-1;i++){
            if(m[i]<=mid) s1+=m[i];
            else s1+=mid;
        }
        printf("Case #%d: %d %d\n",kk,s0,s1);
    }
    return 0;
}
