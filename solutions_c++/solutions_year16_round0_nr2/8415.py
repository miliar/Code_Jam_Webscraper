#include<bits/stdc++.h>
#define MAX 100005

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cases=1;cases<=t;cases++)
    {
        string str;
        cin>>str;

        int len = str.length(),ans=0,cnt = 0;
        if(str[cnt]=='-')
        {
            ans++;
            while(str[cnt]=='-')
                cnt++;
        }


        for(int i=cnt;i<len;)
        {
            while(str[i]=='+')
                i++;
            if(i==len)
                break;
            while(str[i]=='-')
                i++;
            ans+=2;
        }
        printf("Case #%d: %d\n",cases,ans);

    }

    return 0;
}
