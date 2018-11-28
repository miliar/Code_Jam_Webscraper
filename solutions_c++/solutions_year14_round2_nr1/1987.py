#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;
char strs[111][111];
int keys[111][111];
char  sign[1000];
int n;
bool cmps()
{
    char tmp[1111];
    int is=1;
    for(int i=1;i<n && is;i++)
    {
        int tmp_len=strlen(strs[i]);
        char cur=0;int p=0;
        for(int j=0;j<tmp_len;j++)
        {
            if(strs[i][j]!=cur)
            {
                cur=strs[i][j];
                tmp[p++]=cur;
                keys[i][p-1]++;
            }
            else keys[i][p-1]++;
        }
        tmp[p]=0;
        if(strcmp(tmp,sign))   is=0;
    }
    return is;
}
int main()
{
    int T;cin>>T;
    for(int cases=1;cases<=T;cases++)
    {
        memset(keys,0,sizeof(keys));
        cin>>n;
        for(int i=0;i<n;i++) scanf("%s",strs[i]);
        int tmp_len=strlen(strs[0]);
        char cur=0;int p=0;
        for(int i=0;i<tmp_len;i++)
        {
            //cout<<p<<endl;
            if(strs[0][i]!=cur)
            {
                cur=strs[0][i];
                sign[p++]=cur;
                keys[0][p-1]++;
            }
            else keys[0][p-1]++;
        }
        //for(int i=0;i<strlen(sign);i++)cout<<keys[0][i];
        sign[p]=0;
        int is=cmps();
        if(is) 
        {
            int len=strlen(sign);
            int anss[101]={0};
            for(int j=0;j<len;j++)
                for(int i=0;i<n;i++)
                    anss[j]+=keys[i][j];
            for(int i=0;i<len;i++) anss[i]/=n;//cout<<anss[i]<<endl;
            int ans=0;
            for(int j=0;j<len;j++)
                for(int i=0;i<n;i++)
                {
                    ans+=abs(keys[i][j]-anss[j]);
                }
            printf("Case #%d: %d\n",cases,ans);
        }
        else printf("Case #%d: Fegla Won\n",cases);
    }    
    return 0;
}