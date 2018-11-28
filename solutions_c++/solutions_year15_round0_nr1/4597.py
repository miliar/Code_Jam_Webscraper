#include<bits/stdc++.h>
using namespace std;
int X=0,t,n,i,cnt,len,val;
char s[1005];
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {X++;
    cnt=0;
        scanf("%d",&n);
        scanf("%s",s);
        cnt=0;
        len=strlen(s);
        len=n+1;
        val=0;
        for(i=0;i<len;i++)
        {
           if(i>val && s[i]!='0')
            {cnt=cnt+(i-val);
            val=i+(s[i]-'0');
            }
            else
                val=val+s[i]-'0';
        }
    printf("Case #%d: %d\n",X,cnt);
    }
return 0;
}
