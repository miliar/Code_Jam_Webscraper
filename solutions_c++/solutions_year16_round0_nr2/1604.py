//#include <iostream>
//#include <cstdio>
//#include <cstring>
//#include <algorithm>
//using namespace std;
//
//int main()
//{
//    freopen("D.in","r",stdin);
//    freopen("D.out","w",stdout);
//    int t,k,c,s;
//    scanf("%d",&t);
//    for (int cas=1;cas<=t;++cas)
//    {
//        printf("Case #%d: ",cas);
//        scanf("%d%d%d",&k,&c,&s);
//        long long n=1;
//        for (int i=1;i<=c;++i) n*=k;
//        if (s==k)
//            for (int i=1;i<=s;++i)
//                printf("%I64d%c",1+n/k*(i-1),i==s?'\n':' ');
//    }
//    return 0;
//}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int t;
    char s[999];
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        printf("Case #%d: ",cas);
        scanf("%s",s);
        int dif=0;
        for (int i=0;s[i];++dif)
        {
            int j;
            for (j=i+1;s[j]==s[i];++j);
            i=j;
        }
        if (s[0]=='-') printf("%d\n",dif%2==1?dif:dif-1);
        else printf("%d\n",dif%2==1?dif-1:dif);
    }
    return 0;
}
