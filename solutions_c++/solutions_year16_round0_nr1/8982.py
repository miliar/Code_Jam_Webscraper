#include <bits/stdc++.h>
using namespace std;
long long int ques[100005];
int main()
{
    FILE *f,*fp;
    long long int t,n,arr[11],i=0;
    f=fopen("A-large.in","r");
    fp=fopen("output.txt","w");
    while(!feof(f))
    {
        fscanf(f,"%lld",&ques[i]);
        i++;
    }
    for(long long int i=1;i<=ques[0];i++)
    {
        memset(arr,0,sizeof(arr));
        n=ques[i];
        long long int flag=1,ans=n,counti=0,temp=n,defaul=n;
        if(n==0)
            flag=0;
        while(flag)
        {
            // cout<<n<<endl;
            temp=n;
            while(temp!=0)
            {
                int curr=temp%10;
                temp/=10;
                if(arr[curr]==0)
                {
                    arr[curr]=1;
                    counti++;
                }
                if(counti==10)
                {
                    flag=0;
                    ans=n;
                    break;
                }
            }
            n+=defaul;
        }
        if(ans==0)
            fprintf(fp,"Case #%lld: INSOMNIA\n",i);
        else
            fprintf(fp,"Case #%lld: %lld\n",i,ans);
    }
    return 0;
}
