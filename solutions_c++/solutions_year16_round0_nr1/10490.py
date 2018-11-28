#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input_file.txt","r",stdin);

    freopen("output_file.txt","w",stdout);
    int test;
    cin>>test;

    for(int i=0;i<test;i++)
    {
        int visited[12]={0};
        long long int n,count=0,j=1,sum,a,ans;
        cin>>n;
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",i+1);continue;
        }
        while(count<=10)
        {
            sum=n*j;
            ans=sum;

            int len=floor(log10(sum))+1;
            for(int k=1;k<=len;k++)
            {

                a=sum%10;
                sum/=10;
                if(visited[a]==0){visited[a]=1;count++;}
            }
            if(count==10)
            {
                printf("Case #%d: %lld\n",i+1,ans);break;
            }
            j++;
        }
    }

    return 0;

}
