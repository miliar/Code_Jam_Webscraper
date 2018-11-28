#include<cstdio>
int divisor[11];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    puts("Case #1:");
    for(int num=(1<<15)+(1<<0),cnt=0;cnt<50;num+=2)
    {
        bool flag=true;
        for(int i=2;i<=10;i++)
        {
            long long t = 0;
            long long k = 1;
            for(int j=0;j<=15;j++,k*=i)
                t += ((num&(1<<j))>>j)*k;
            bool found=false;
            for(int j=2;j<=10000;j++)
                if(t % j == 0) { divisor[i]=j; found = true; break; }
            if(!found){ flag=false; break; }
        }
        if(flag)
        {
            cnt++;
            for(int j=15;j>=0;j--)
                printf((num&(1<<j))?"1":"0");
            for(int j=2;j<=10;j++)
                printf(" %d",divisor[j]);
            puts("");
        }
    }

    return 0;
}
