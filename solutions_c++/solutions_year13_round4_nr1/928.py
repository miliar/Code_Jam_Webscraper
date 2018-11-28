#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
int t,n,m,nub,nub2;
struct node {
        int o,e,p;
}tra[1005];
long long dis,amount;
struct node2 {
        int at,type,num;
        bool operator < (const node2 &o) const {
                if(at!=o.at) return at<o.at;
                return type<o.type;
        }
}event[4005],b[4005];
int main()
{
        freopen("A-small-attempt1.in","r",stdin);
        freopen("out.txt","w",stdout);
        scanf("%d",&t);
        for(int r=1;r<=t;r++)
        {
                amount=0;
                nub=0;nub2=-1;
                scanf("%d %d",&n,&m);
                for(int i=0;i<m;i++)
                {
                        scanf("%d %d %d",&tra[i].o,&tra[i].e,&tra[i].p);
                        dis = tra[i].e-tra[i].o;
                        amount+=dis*(2*n-dis+1)/2*tra[i].p;
                        //printf("%I64d\n",amount);
                        amount%=1000002013;
                        event[nub].type=0;
                        event[nub].at=tra[i].o;
                        event[nub].num=tra[i].p;
                        nub++;
                        event[nub].type=1;
                        event[nub].at=tra[i].e;
                        event[nub].num=tra[i].p;
                        nub++;
                //printf("DDDD%d %d\n",r,nub);
                }
                sort(&event[0],&event[nub]);
                //printf("EEEE%d %d\n",r,nub);
                for(int i=0;i<nub;i++)
                {
                        //printf("event %d %d %d\n",event[i].at,event[i].type,event[i].num);
                        if(event[i].type==0)
                        {
                                nub2++;
                                b[nub2].at=event[i].at;
                                b[nub2].num=event[i].num;
                        }
                        else
                        {
                                while(event[i].num!=0)
                                {
                                        //if(nub2==-1) printf("
                                        //printf("Found %d %d\n",b[nub2].at,b[nub2].num);
                                        if(b[nub2].num<=event[i].num)
                                        {
                                                dis = event[i].at-b[nub2].at;
                                                amount-=dis*(2*n-dis+1)/2*b[nub2].num;
                                                amount%=1000002013;
                                                if(amount<0) amount+=1000002013;
                        //printf("DD %I64d\n",amount);
                                                event[i].num-=b[nub2].num;
                                                nub2--;
                                        }
                                        else
                                        {
                                                dis = event[i].at-b[nub2].at;
                                                amount-=dis*(2*n-dis+1)/2*event[i].num;
                                                amount%=1000002013;
                                                if(amount<0) amount+=1000002013;
                        //printf("DD %I64d\n",amount);
                                                b[nub2].num-=event[i].num;
                                                event[i].num=0;
                                        }
                                }
                        }
                }                               
                printf("Case #%d: %I64d\n",r,amount);
        }
        //system("pause");
}
