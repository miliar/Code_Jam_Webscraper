#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    int arr[10];

    for(int k=1;k<=tc;k++)
    {
        string s;
        cin>>s;
        int n = s.size();
        string tmp = s;
        sort(tmp.begin(),tmp.end());
        if(tmp[0]==tmp[n-1])
        {
            if(tmp[0]=='-')
                printf("Case #%d: 1\n",k);
            else printf("Case #%d: 0\n",k);
            continue;
        }
        int ans = 0;
        while(1)
        {
            tmp = "";
            int f=0;
            ans++;
            char c = s[0];
            for(int i=0;i<n;i++)
            {
                if(c == s[i])
                {
                    if(s[i]=='+') s[i]='-';
                    else s[i]='+';
                }
                else break;
            }
            for(int i=0;i<n;i++)
            {
                if(s[i]=='-') f=1;
            }
            if(f==0)
            {
                break;
            }

        }

        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
