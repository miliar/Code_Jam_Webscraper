#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAXN 1100
using namespace std;

double Naomi[MAXN],Ken[MAXN];
bool check[MAXN];

bool cmp(const double &o1, const double &o2)
{
    return o1>o2;
}

int main()
{
    int t,kase,n,i,score_war,score_cheat,o2i,o2j,j;
    scanf("%d",&t);
    for(kase=1;kase<=t;kase++)
    {
        memset(check,false,sizeof(check));
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%lf",&Naomi[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&Ken[i]);
        sort(Naomi,Naomi+n,cmp);
        sort(Ken,Ken+n);
        score_war=score_cheat=0;
        o2i=0;o2j=n-1;
        for(i=0;i<n;i++)
        {
            if(Naomi[i]>Ken[o2j])
            {
                check[o2i]=true;
                o2i++;
                score_war++;
            }
            else
            {
                for(j=o2j-1;j>=o2i;j--)
                {
                    if(check[j])    continue;
                    if(Naomi[i]>Ken[j])
                        break;
                }
                j++;
                while(check[j]){       j++;  }
                check[j]=true;
                while(check[o2i]){     o2i++; }
                while(check[o2j]){     o2j--; }
            }
        }
        o2i=0;o2j=n-1;
        for(i=n-1;i>=0;i--)
        {
            if(Naomi[i]>Ken[o2i]){
                o2i++;
                score_cheat++;
            }
            else
                o2j--;
        }
        cout<<"Case #"<<kase<<": "<<score_cheat<<" "<<score_war<<endl;
    }
    return 0;
}
