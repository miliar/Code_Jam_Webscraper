#include <bits/stdc++.h>
#define gc getchar_unlocked
#define LL long long
#define MOD 1000000007
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a_ans2.txt","w",stdout);
    int t,n,p;
    char s[1005];
    scanf("%d",&t);
    for(int k=1; k<=t;k++)
    {
        scanf("%d%s",&n,&s);
        int person=0, need=0,extra=0;
        for(int i=0; i<strlen(s); i++)
        {
            if(i>person && s[i]!='0')
            {
                need=i-person;
                extra+=need;
                person+=need;
            }
            person+= (s[i]-'0');
        }
        printf("Case #%d: %d\n",k,extra);
    }
    return 0;
}
