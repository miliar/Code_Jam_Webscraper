#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
bool check[10];
int dig;
void calc(int x)
{
        while (x>0)
        {
                if (!check[x%10]) dig++;
                check[x%10]=true;
                x/=10;
        }
}
void work()
{
        memset(check,0,sizeof(check));
        int n;
        scanf("%d",&n);
        if (n==0)
        {
                cout<<"INSOMNIA"<<endl;
                return;
        }
        dig=0;
        int now=0;
        while (1)
        {
                now+=n;
                calc(now);
                if (dig==10) break;
        }
        cout<<now<<endl;
}
int main()
{
        int T,cas=0;
        scanf("%d",&T);
        while (T--)
        {
                printf("Case #%d: ",++cas);
                work();
        }
}
