#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("TasnimIN.txt","r",stdin);
    freopen("TasnimOUT.txt","w",stdout);
    long long n,i=1,r,c,temp,k,cnt,temp2;
    int mark[11];
    scanf("%lld",&c);
    for(k=1;k<=c;k++){
    memset(mark,0,sizeof mark);
    cnt=0;
    i=1;
    scanf("%lld",&n);
    temp2=n;
    while(1)
    {
        i++;
        temp=temp2;
        while(temp){
        r=temp%10;
        temp/=10;
        if(mark[r]==0)
        {
            cnt++;
            mark[r]=1;
        }
        }
        //cout << cnt << " " << n << endl;
        if(cnt==10|| n==0)
            break;
        temp2=n*i;
    }
    if(cnt==10)
    printf("Case #%lld: %lld\n",k,temp2);
    else printf("Case #%lld: INSOMNIA\n",k);
    }
}
