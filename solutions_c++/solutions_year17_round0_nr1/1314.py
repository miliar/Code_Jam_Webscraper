#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <queue>

#define MEM(a,x) memset(a,x,sizeof a)
#define eps 1e-8
#define MOD 10009
#define MAXN 10010
#define MAXM 100010
#define INF 99999999
#define ll __int64
#define bug cout<<"here"<<endl
#define fread freopen("A-large.in","r",stdin)
#define fwrite freopen("out.txt","w",stdout)

using namespace std;

int main()
{
//    fread;
//    fwrite;
    int tc;
    scanf("%d ",&tc);
    char ch[1010];
    int a[1010];
//    gets(ch);
    int cs=1;
    while(tc--)
    {
        scanf("%s",ch);
        int k;
        scanf("%d",&k);
        int ans=0;
        int len=strlen(ch);
        MEM(a,0);
        for(int i=0;i<len;i++)
        {
            if(ch[i]=='+')
                a[i]=1;
        }
//        for(int i=0;i<len;i++)
//            cout<<a[i];
//        cout<<endl;
        for(int i=0;i<len;i++)
        {
            if(a[i]==0&&(i+k-1)<len)
            {
                for(int j=0;j<k;j++)
                {
                    a[i+j]=1-a[i+j];
                }
                ans++;
            }

        }
//        for(int i=0;i<len;i++)
//            cout<<a[i];
//        cout<<endl;
        for(int i=0;i<len;i++)
        {
            if(!a[i])
                ans=-1;
        }
        printf("Case #%d: ",cs++);
        if(ans>=0)
            printf("%d\n",ans);
        else
            printf("IMPOSSIBLE\n");
    }

    return 0;
}
