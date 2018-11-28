#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
const int MOD=1000000007;
#define ll long long
const int N=1010;
char s[N];
int a[N];
int main()
{
    FILE *fpt;
    int T;
    scanf("%d",&T);
    int cas=1;
    fpt = fopen("res.txt","w");//打开文档，写入
    while(T--)
    {
        int n;
        scanf("%d",&n);
        scanf("%s",s);
        for(int i=0;i<=n;i++)
        {
            a[i]=s[i]-'0';
        }
        int ans=0;
        int temp=a[0];
        for(int i=1;i<=n;i++)
        {
            if(i>temp)
            {
                ans+=(i-temp);
                temp+=(i-temp);
            }
             temp+=a[i];
        }


        fprintf(fpt,"Case #%d: %d\n",cas++,ans);


        //printf("Case #%d: %d\n",cas++,ans);
    }fclose(fpt);
    return 0;
}





















