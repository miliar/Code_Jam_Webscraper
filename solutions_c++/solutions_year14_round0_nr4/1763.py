#include <stdio.h>
#include <stdlib.h>
#include <list>

using namespace std;

#define BOLCK_EXIST         1
#define BOLCK_FIRED         0
#define NAOMI               1
#define KEN                 -1

class Block
{
public:
    double mass;    // 0-1.0
    int belong;     // 1 is naomi, -1 is ken

public:
    bool operator < (const Block &b)const
    {
        return mass < b.mass;
    }
};

void showlist(list<Block> lst)
{
    printf("All Blocks:\n");
    for (list<Block>::iterator it= lst.begin();it!=lst.end();it++)
    {
        printf("    %.5f(%2d)\n",(*it).mass,(*it).belong);
    }
}

int main()
{
    int t,n;
    list<Block> ab;

    //freopen ("D-small-attempt0.in","r",stdin);
    //freopen ("D-small-attempt0.out","w",stdout);
    freopen ("D-large.in","r",stdin);
    freopen ("D-large.out","w",stdout);

    scanf("%d",&t);
    for (int ti=1;ti<=t;ti++)
    {
        scanf("%d",&n);
        ab.clear();
        for (int i=0;i<n;i++)
        {
            Block b;
            scanf("%lf",&(b.mass));
            b.belong=NAOMI;
            ab.push_back(b);
        }
        for (int i=0;i<n;i++)
        {
            Block b;
            scanf("%lf",&(b.mass));
            b.belong=KEN;
            ab.push_back(b);
        }

        ab.sort();

        // play war
        list<Block> bw (ab);
        list<Block>::iterator it0 = bw.begin();
        list<Block>::iterator it1 = bw.begin();
        it1++;
        while(it0!=bw.end() && it1!=bw.end())
        {
            while (bw.size()>0 && (*it0).belong == NAOMI && (*it1).belong == KEN)
            {
                //printf(" war: [%2d](%.5f) and [%2d](%.5f) size=%d\n",(*it0).belong,(*it0).mass,(*it1).belong,(*it1).mass,bw.size());
                it1=bw.erase(it1);
                it0=bw.erase(it0);
                if (it0==bw.begin()) it1++;
                else it0--;
            }
            it0++;
            it1++;
        }
        int war = bw.size()/2;
        //printf("war=%d\n",war);

        // play Deceitful War
        int dwar = 0;
        list<Block> dw (ab);
        it0 = dw.begin();
        it1 = dw.begin();
        it1++;
        while (it0!=dw.end() && it1!=dw.end())
        {
            while (dw.size()>0 && (*it0).belong == KEN && (*it1).belong == NAOMI)
            {
                //printf("dwar: [%2d](%.5f) and [%2d](%.5f) size=%-4d dwar=%d\n",(*it0).belong,(*it0).mass,(*it1).belong,(*it1).mass,dw.size(),dwar);
                dwar++;
                it1=dw.erase(it1);
                it0=dw.erase(it0);
                if (it0==dw.begin()) it1++;
                else it0--;
            }
            it0++;
            it1++;
        }

        printf("Case #%d: %d %d\n",ti,dwar,war);
    }

    fclose(stdout);
    fclose(stdin);
    return 0;
}
