#include<cstdio>
using namespace std;
int Q,n,t,s,c,i,rez;
char s1[1004];
int main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    scanf("%d\n",&Q);
    while(Q)
    {
        t++;
        printf("Case #%d: ",t);
        Q--;
        scanf("%d ",&n);
        gets(s1);
        rez=0;
        s=s1[0]-'0';
        for(i=1;i<=n;i++)
        {
            c=s1[i]-'0';
            if(s<i&&c!=0){rez+=(i-s);s+=rez;}
            s+=c;
        }
        printf("%d\n",rez);
    }
}
