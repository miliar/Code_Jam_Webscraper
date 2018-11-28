#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int isit[15];

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t;
    cin>>t;
    for(int ca=1;ca<=t;ca++){
        int n,cnt=0,gun=1,temp,ans;
        memset(isit,0,sizeof(isit));
        printf("Case #%d: ",ca);
        cin>>n;
        if(!n){
            printf("INSOMNIA\n");
            continue;
        }
        while(cnt<10){
            ans=gun*n;
            temp=ans;
            while(temp){
                if(!isit[temp%10])
                    cnt++;
                isit[temp%10]=1;
                temp/=10;
            }
            gun++;
        }
        printf("%d\n",ans);
    }
    return 0;
}
