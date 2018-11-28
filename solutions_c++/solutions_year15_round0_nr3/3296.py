#include<bits/stdc++.h>
#define pb push_back
#define tr(c,i) for(typeof((c).begin() )i = (c).begin(); i != (c).end(); i++)
#define mod 1000000007
#define ii  pair<int,int>

using namespace std;
typedef long long ll;



using namespace std;

int cmp(const void *a,const void *b)
{
    return *(int *)b-*(int *)a;
}

char s[10010];

int main()
{
    int i,j,k,l,m,n,x,cnt=0,lm,sign,t,tst,fl;
    char p,tg;

freopen("C-small-attempt0.in", "r", stdin);
freopen("COUT-small-attempt0.txt", "w", stdout);
scanf("%d",&t);
for(tst=1;tst<=t;tst++)
{
     scanf("%d%d",&l,&x);
     scanf("%s",&s);
     cnt=0;lm=l*x;
     p='1';sign=fl=0;tg='i';
     for(cnt=0,i=0;cnt<lm;cnt++,i++)
     {
         if(p=='1')
         p=s[i];
         else if(p==s[i])
         {
             p='1';
             sign++;
         }
         else if(p=='i')
         {
             if(s[i]=='j')
             p='k';
             else
             {
                 p='j';
                 sign++;
             }
         }
          else if(p=='j')
         {
             if(s[i]=='k')
             p='i';
             else
             {
                 p='k';
                 sign++;
             }
         }
          else if(p=='k')
         {
             if(s[i]=='i')
             p='j';
             else
             {
                 p='i';
                 sign++;
             }
         }
         if(sign%2==0&&tg=='i'&&p==tg)
         { tg='j';p='1';}
          else if(sign%2==0&&tg=='j'&&p==tg)
         {tg='k';p='1';}
          else if(sign%2==0&&tg=='k'&&p==tg)
         {
             /*if(cnt!=lm-1)
             tg='1';
             else
             {fl=1;cout<<"got k\n";}*/
             if(cnt==lm-1)
             fl=1;
         }
         if(i==l-1)
         i=-1;


     }

    if(fl)
     printf("Case #%d: %s\n",tst,"YES");
    else
     printf("Case #%d: %s\n",tst,"NO");
}



    return 0;
}
