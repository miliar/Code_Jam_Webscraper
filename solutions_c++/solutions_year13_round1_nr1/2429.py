#include<iostream>
//#include<conio.h>
using namespace std;
int main()
{
    int test,co=1;
    long long r,t;
    scanf("%d",&test);
    while(test--)
    {
        scanf("%lld%lld",&r,&t);
        long long ans=0,x=1,y=0,m;
        while(1)
        {
            m=(((r+x)*(r+x))-((r+y)*(r+y)));
            if(t>=m)
            {
                t=t-m;
                ans++;
            }
            else
                break;
            x=x+2;
            y=y+2;
        }
        cout<<"Case #"<<co<<": "<<ans<<endl;
        co++;
        ans=0;
    }
    //getch();
    return 0;
}
