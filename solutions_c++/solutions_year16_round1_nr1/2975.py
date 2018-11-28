#include <bits/stdc++.h>

using namespace std;

#define LL long long

int main()
{
    int T;
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
            printf("Case #%d: ",t);
            char str[2100], ans[1100];

            scanf(" %s",str);
            int n = strlen(str);

            for(int i=0;i<n;i++)
                str[i+n] = str[i];

            int l = n;
//            cout<<l<<' ';
            for(int i=1;i<n;i++)
                if(str[i+n]>=str[l])
                {
//                    cout<<str[i]<<' ';
                    l--;
                    str[l] = str[i+n];
//                    cout<<str[l]<<' ';
                    str[i+n] = 0;
                }
//            cout<<l<<' '<<str[l];
            int i=0;
            while(i<n)
            {
                if(str[l]>0)
                {
                    ans[i] = str[l];
//                    cout<<l<<' '<<ans[i]<<' ';
                    i++;
                }
                l++;
            }
            ans[i] = '\0';
            printf("%s\n",ans);
    }
    return 0;
}
