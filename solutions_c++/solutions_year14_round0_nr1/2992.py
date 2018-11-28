#include <cstdio>
#include <map>
using namespace std;
int t, i, j, buf, bufv, cnt;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for(int l=1; l<=t; l++)
    {
        map<int,bool> m;
        cnt=0;
        scanf("%d",&i);
        for(int r=1; r<5; r++)
        {
            for(int c=1; c<5; c++)
            {
                scanf("%d",&buf);
                if(r==i) m[buf]=true;
            }
        }
        scanf("%d",&j);
        for(int r=1; r<5; r++)
        {
            for(int c=1; c<5; c++)
            {
                scanf("%d",&buf);
                if(r==j)
                {
                    if(m[buf]==true)
                    {
                        cnt++;
                        bufv=buf;
                    }
                }
            }
        }
        printf("Case #%d: ",l);
        if(cnt==1) printf("%d",bufv);
        else if(cnt==0) printf("Volunteer cheated!");
        else printf("Bad magician!");
        printf("\n");
    }
}
