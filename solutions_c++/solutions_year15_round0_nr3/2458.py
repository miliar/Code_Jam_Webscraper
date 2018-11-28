#include <bits/stdc++.h>
using namespace std;

const int N=80010;
char str[N];
typedef long long ll;

int sign,cur;
void com(int op)
{
    if(cur==1)
    {
        cur=op;
        return;
    }
    if(cur==op)
    {
        cur=1;
        sign=(sign+1)%2;
        return;
    }
    if(cur=='i'&&op=='j')
    {
        cur='k';
        return;
    }
    if(cur=='i'&&op=='k')
    {
        cur='j';
        sign=(sign+1)%2;
        return;
    }
    if(cur=='j'&&op=='k')
    {
        cur='i';
        return;
    }
    if(cur=='j'&&op=='i')
    {
        cur='k';
        sign=(sign+1)%2;
        return;
    }
    if(cur=='k'&&op=='i')
    {
        cur='j';
        return;
    }
    if(cur=='k'&&op=='j')
    {
        cur='i';
        sign=(sign+1)%2;
        return;
    }
}
int main()
{
    freopen("C1.in","r",stdin);
    freopen("C2.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cs=1;cs<=t;cs++)
    {
        ll length,repeats;
        scanf("%lld%lld",&length,&repeats);
        scanf("%s",str);
   //     if(repeats>8)
   //         repeats=8;
        for(int iter=2,i=0,j=length;iter<=repeats;)
        {
            str[j]=str[i];
            i++;
            j++;
            if(i==length)
            {
                i=0;
                iter++;
            }
        }
        length*=repeats;
        sign=0;
        cur=1;
        bool fi=false,fk=false;
        for(int i=0;i<length;i++)
        {
            com(str[i]);
            if(sign==0&&cur=='i')
                fi=true;
            else if(sign==0&&cur=='k'&&fi)
                fk = true;
      //      printf("%d %d\n",cur,sign);
        }
        bool ans=(fi&&fk&&cur==1&&sign==1);
        printf("Case #%d: %s\n",cs,(ans?"YES":"NO"));
    }
    return 0;
}
