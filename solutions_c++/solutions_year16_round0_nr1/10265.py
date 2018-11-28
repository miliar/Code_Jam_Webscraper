#include<bits/stdc++.h>
using namespace std;
int ch[10]={0};
bool is_cheak(long long int n)
{
    int i,temp,counter=0,digit;
    temp=n;
    while(temp>0)
    {
        digit=temp%10;
        ch[digit]=1;
        temp=temp/10;
    }
    for(i=0;i<10;i++){
        //printf("%d %d %lld\n",i,ch[i],n);
        if(ch[i]==1)
            counter++;
    }
    //printf("%d\n",counter);
    if(counter==10)
        return true;
    else
        return false;

}
int main()
{
    int t,d=1;
    scanf("%d",&t);
    while(t--)
    {

        long long int temp,n,ans=-101,i,j;
         for(i=0;i<10;i++)
            ch[i]=0;
        scanf("%lld",&n);
        for(i=1;i<=200;i++)
        {
            temp=n*i;
            if(is_cheak(temp)==true){
                ans=temp;
                //printf("flag 1\n");
                break;
            }
        }
        if(ans!=-101)
            printf("Case #%d: %lld\n",d,ans);
        else
            printf("Case #%d: INSOMNIA\n",d);
        d++;
    }
    return 0;
}
