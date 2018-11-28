#include<bits/stdc++.h>
#define getcx getchar
using namespace std;
inline void inp( int &n )
 {
    n=0;
    int ch=getcx();int sign=1;
    while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}

    while(  ch >= '0' && ch <= '9' )
            n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
    n=n*sign;
  }

int main()
{
    int t,n,S,j,total,ans,i;
    char s[10000];

    inp(t);//scanf("%d",&t);

    for(j=1;j<=t;j++)
    {

       inp(S);
       scanf("%s",&s);
        ans=i=total=0;
        while(s[i])
        {
            if(total<i)
            {
                ans += i-total;
                total += i - total;
            }
            //else
                total+=s[i]-'0';

            i++;
        }

        printf("Case #%d: %d\n",j,ans);
    }
    return 0;
}
