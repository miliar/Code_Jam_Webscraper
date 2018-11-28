#include<stdio.h>
#include<vector>
#include<set>
using namespace std;
int main()
{
    int T,N,M;
    freopen("A-large.in","r",stdin);
    freopen("xxx.out","w",stdout);
    scanf("%d",&T);
    int tt=1;
    int i,j,k;
    while(T--)
    {
        multiset<int> s;
        multiset<int>::iterator it;
        scanf("%d%d",&N,&M);
        for(i=0;i<N;i++)
        {
            scanf("%d",&k);
            s.insert(k);
        }
        int Mc=0;
        while(!s.empty())
        {
            i=*(s.begin());
            k=M-i;
            it=s.upper_bound(k);
            //printf("%d %d\n",i,k);
            if(it!=s.begin())
                it--;
            j=(*it);
            if(it!=s.begin() && i+j<=M)
            {
                //printf("%d]\n",j);
                Mc++;
                s.erase(it);
                s.erase(s.begin());
            }
            else
            {
                Mc++;
                s.erase(it);
            }
        }
        printf("Case #%d: %d\n",tt,Mc);
        tt++;
    }
}
