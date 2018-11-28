#include<cstdio>
#include<cstdlib>
#include<cstdlib>
#include<cmath>
#include<set>
#include<algorithm>

using namespace std;
#define x first
#define y second
#define pdd pair<double , double>
double solve(double c,double f,double x)
{
    set<pdd> heap;
    heap.clear();
    heap.insert(pdd(0,2));
    while(!heap.empty())
    {
        pdd node = *(heap.begin());
        heap.erase(heap.begin());
        if(node.y == 0)
            return node.x;
        heap.insert(pdd(node.x+(c/node.y),(node.y+f)));
        heap.insert(pdd(node.x+(x/node.y) , 0));
    }
    return 0;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outB.txt","w",stdout);
    int tCase;
    double c,f,x;
    scanf("%d",&tCase);
    for(int tt = 1;tt<=tCase;tt++)
    {
        printf("Case #%d: ",tt);
        scanf("%lf %lf %lf",&c,&f,&x);
        printf("%.7lf\n",solve(c , f, x));
    }
    


    return 0;
}