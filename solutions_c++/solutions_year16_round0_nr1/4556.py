#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#define ll long long


using namespace std;

int main()
{
    freopen("0in.txt","r",stdin);
    freopen("0out.txt","w",stdout);
    int i,j,k,t;
    int vis[11];
    ll num,p,num1;
    scanf("%d",&t);

    for(int kk1=1;kk1<=t;kk1++)
    {
        scanf("%lld",&num);
        memset(vis,0,sizeof(vis));
     //   Case #1: INSOMNIA
        printf("Case #%d: ",kk1);
        if(num==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        int cnt,dig;
        cnt=0;
        num1=num;
        for(i=1;;i++)
        {


            if(cnt==10)
            {
                break;
            }
            num=num1*i;
        //    cout<<num<<endl;

            p=num;
            while(p)
            {
                dig=p%10;
                if(vis[dig]==0)
                {
                    vis[dig]=1;
                    cnt++;
                }
                p=p/10;
            }

        }

        cout<<num<<endl;



    }

}
