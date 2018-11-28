#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<vector>

#define pii pair<int,int>
#define F first
#define S second
#define MOD 1000000007
#define itt iterator
#define ritt reverse_iterator
#define LL long long

using namespace std;

char opp(char x)
{
    return x=='+'?'-':'+';
}

int t,l,c,lf;
char s[105],tmp[105];

int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("B-large.out","w",stdout);

    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        scanf("%s",s);
        l=strlen(s)-1;
        c=0;
        while(l!=-1)
        {
            while(s[l]=='+')
            {
                l--;
                if(l==-1)   break;
            }
            if(l==-1)   break;
            c++;
            if(s[0]=='+')
            {
                for(int i=0;s[i]=='+';i++)  s[i]='-';
            }
            else
            {
                for(int i=0;i<=l;i++)   tmp[l-i]=opp(s[i]);
                for(int i=0;i<=l;i++)   s[i]=tmp[i];
            }
        }
        printf("Case #%d: %d\n",z,c);
    }
    return 0;
}
