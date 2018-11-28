#include<cstdio>
#include<set>
#include<utility>
using namespace std;

int main()
{
    int T,c,d,m,n,skor,ans;
    set<int> s;
    scanf("%d",&T);
    for(int tc=1;tc<=T;tc++)
    {
        s.clear();
        scanf("%d",&n);
        for(c=1;c<=4;c++)
        {
            if(c==n) for(d=0;d<4;d++)
            {
                scanf("%d",&m);
                s.insert(m);
            }
            else for(d=0;d<4;d++) scanf("%d",&m);
        }
        skor = 0;
        scanf("%d",&n);
        for(c=1;c<=4;c++)
        {
            if(c==n) for(d=0;d<4;d++)
            {
                scanf("%d",&m);
                if(!s.insert(m).second)
                {
                    skor++;
                    ans = m;
                }
            }
            else for(d=0;d<4;d++) scanf("%d",&m);
        }
        
        if(skor==1) printf("Case #%d: %d\n",tc,ans);
        else if(skor>1) printf("Case #%d: Bad magician!\n",tc);
        else printf("Case #%d: Volunteer cheated!\n",tc);
    }
    return 0;
}
