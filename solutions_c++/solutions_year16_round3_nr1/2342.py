#include<cstdio>
#include<algorithm>
#include<queue>
#include<cstring>
#define maxn 3000
using namespace std;

 struct node
 {
     friend bool operator< (node n1, node n2)
     {
         return n1.val < n2.val;
     }
     int val;
     int pos;
}a[maxn];
int cmp(node x,node y)
{

    if(x.val==y.val)
        return x.pos<y.pos;
    return x.val>y.val;
}
int main()
{
    //freopen("E:A-large (1).in","r",stdin);
    //freopen("E:outA.txt","w",stdout);
    int T,n;
    scanf("%d",&T);
    priority_queue<node> qi;
    for(int ca=1;ca<=T;ca++)

    {
        printf("Case #%d: ",ca);
        while(!qi.empty())
            qi.pop();
        scanf("%d",&n);
        int sum=0;
        for(int i=1;i<=n;i++)
        {

            scanf("%d",&a[i].val);
            a[i].pos=i;
            qi.push(a[i]);
            sum+=a[i].val;
        }
//        sort(a+1,a+1+n,cmp);

//        node fuck,fuck2;
        int now=sum;
        while(now!=3&&now>0)
        {
            node fuck,fuck2;
            fuck=qi.top();
            qi.pop();
            fuck.val--;
            qi.push(fuck);
            printf("%c",fuck.pos+'A'-1);
           // q.pop();
            now--;
            fuck2=qi.top();
            printf("%c",fuck2.pos+'A'-1);
            qi.pop();
            fuck2.val--;
            qi.push(fuck2);
            now--;
            if(now)
            printf(" ");
        }
        if(now==3)
        {
            node fuck;
            fuck=qi.top();
            qi.pop();
            printf("%c ",fuck.pos+'A'-1);
            fuck=qi.top();
            printf("%c",fuck.pos+'A'-1);
            qi.pop();
            fuck=qi.top();
            printf("%c",fuck.pos+'A'-1);
        }
        printf("\n");
    }
}

