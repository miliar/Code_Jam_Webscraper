#include<bits/stdc++.h>
using namespace std;
int main()
{
   freopen("A-large.txt","r",stdin);
    freopen("output.txt","w",stdout);
long long int n,i,x,y;
int e,b;
cin>>b;

for(e=1;e<b+1;e++)
{
    y=0;
    int a[10] = {0};
    cin>>n;
    for(i=1;i<100000;i++)
    {
        y=n*i;
        if(a[9]==1&&a[8]==1&&a[7]==1&&a[6]==1&&a[5]==1&&a[4]==1&&a[3]==1&&a[2]==1&&a[1]==1&&a[0]==1)
        {
            cout<<"Case #"<<e<<": "<<y-n<<endl;
            break;
        }
        while(y>0)
        {
            x=y%10;
            y=y/10;
            if(x==9)
            a[9]=1;
            if(x==8)
                a[8]=1;
            if(x==7)
                a[7]=1;
            if(x==6)
                a[6]=1;
            if(x==5)
                a[5]=1;
            if(x==4)
                a[4]=1;
            if(x==3)
                a[3]=1;
            if(x==2)
                a[2]=1;
            if(x==1)
                a[1]=1;
            if(x==0)
                a[0]=1;
            }
        }
    if( a[9]!=1||a[8]!=1||a[7]!=1||a[6]!=1||a[5]!=1||a[4]!=1||a[3]!=1||a[2]!=1||a[1]!=1||a[0]!=1)
    {
        cout<<"Case #"<<e<<": "<<"INSOMNIA"<<endl;
   }

}
return 0;
    }
