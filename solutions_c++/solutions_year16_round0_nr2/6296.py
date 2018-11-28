#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <algorithm>
#include <cmath>
#include <string>
#include <map>
#include <cmath>
#include <set>
using namespace std;

int main()
{

    int t,j=1;
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    bool flog;
    char ch[10000];
    while(t--)
    {
        scanf("%s",ch);
        printf("Case #%d: ",j++);
        int l=strlen(ch);
        int flog=0;
        for(int i=1;i<l;i++)
        {
            if(ch[i]!=ch[i-1])
            {
                flog=1;
                break;
            }
        }
        if(flog==0&&ch[0]=='-')
        {
            printf("1\n");
            continue;
        }
        long long  cnt=0;
        for(int i=1;i<l;i++)
        {
            if(ch[i]!=ch[i-1])
            {
                int j;
                for( j=i+1;j<l;j++)
                {
                    if(ch[j]!=ch[i])
                        break;
                }
                if(ch[i]=='-')
                {
                    cnt+=2;
                    ch[j-1]='+';
                }
                else
                    cnt+=1;

                i=j-1;
            }
        }
        printf("%lld\n",cnt);

    }
//        if(ch[0]=='+')
//        {
//            for(int i=1; i<l; i++)
//            {
//                if(ch[i]!=ch[i-1])
//                    cnt++;
//            }
////            if(ch[l-1]=='-')
////                printf("%lld\n",cnt*2);
////            else
//                printf("%lld\n",cnt*2);
//        }
//        else
//        {
//            for(int i=1; i<l; i++)
//            {
//                if(ch[i]!=ch[i-1])
//                    cnt++;
//            }
//            if(cnt==0)
//                printf("1\n");
//            else
//                printf("%lld\n",cnt*2-1);
//        }
//    }
}
