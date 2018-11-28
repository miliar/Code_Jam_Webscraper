#include<iostream>
#include<cstdio>
using namespace std;
char s[1002];
int a[1002];
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int n,sum=0,counter=0;
        scanf("%d%s",&n,&s);
        for(int j=0;j<=n;j++)
        {
            a[j]=s[j]-'0';//cout<<a[j];
        }
       // cout<<n<<" "<<s<<"\n";
        for(int x=0;x<=n;x++)   
        {
            sum+=a[x];
            if(x>=sum)
                {counter+=1;
                sum+=1;
                //cout<<"sum:"<<sum<<" count:"<<counter<<" x:"<<x<<"\n";
                }
           }
        printf("Case #%d: %d\n",i,counter);
    }
return 0;
}       

