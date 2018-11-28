#include<iostream>
#include<conio.h>
#include<math.h>
#include<stdio.h>
bool checkp(int);
using namespace std;
int main()
{
    int n,a,b,x,y,ca=1,count;
    freopen( "C-small-attempt0.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
    cin>>n;
    while(ca<=n)
    {
    count=0;
    cin>>a>>b;
    x=sqrt(a);
    if(x*x<a) x++;
    y=sqrt(b);
    for(int i=x; i<=y;i++)
    {
            if(checkp(i))
            {if (checkp(i*i))
            {

            count++;
            }
            }

    }
    cout<<"Case #"<<ca<<": "<<count<<endl;
    ca++;
    }

    return 0;
}
bool checkp(int n)
{
     int num=n,newn=0;
     int r;
     while(num!=0)
     {
     r=num%10;
     num/=10;
     newn=newn*10+r;
     }
     if (newn==n) {return true;}
     else return false;
}
