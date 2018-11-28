#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
using namespace std;


int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;
    cin>>tc;
    int standUp=0,maxShy=0,x,y,invited=0,a[1001];
    for(int i=1;i<=tc;i++)
    {
        standUp=0,maxShy=0,invited=0;
        cin>>maxShy;
        cin>>x;
        for(int j=maxShy;j>=0;j--)
        {
            a[j]=x%10;
            x=x/10;
        }
        if(a[0]>0) standUp+=a[0];
        for(int j=1;j<=maxShy;j++)
        {

            x=a[j];

            if(x>0)
            {
                if(standUp>=j)
                    standUp+=x;

                else
                {
                    y=j-standUp;
                    invited+=y;
                    standUp= standUp + y + x;
                }
                 ;
            }
        }
        cout<<"Case #"<<i<<": "<<invited<<endl;

    }
    return 0;
}
