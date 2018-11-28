#include<bits/stdc++.h>
using namespace std;
long long int seen1,seen2,seen3,seen4,seen5,seen6,seen7,seen8,seen9,seen0;
long long int num(long long int x)
{
    long long int y,j,z;
    while(x>0)
    {
       y=x%10;
       x=x/10;
       if(y==1)
           seen1=1;
       if(y==2)
       seen2=1;
       if(y==3)
       seen3=1;
       if(y==4)
       seen4=1;
       if(y==5)
       seen5=1;
       if(y==6)
       seen6=1;
       if(y==7)
       seen7=1;
       if(y==8)
       seen8=1;
       if(y==9)
       seen9=1;
       if(y==0)
       seen0=1;
    }


}
int main()
{
    long long int t,n,k=0,i,j,x;

    ifstream in;
    in.open("abc.txt");
    ofstream out;
    out.open("abc2.txt");
    in>>t;
    k=1;
    while(t--)
    {

        seen1=0;seen2=0;seen3=0;seen4=0;seen4=0;seen5=0;seen6=0;seen7=0;seen8=0;seen9=0;
        seen0=0;
        in>>n;
        if(n==0)
        out<<"Case #"<<k<<": INSOMNIA"<<endl;
        else{
        for (i=1;i<=10000000;++i)
        {
           x=n*i;

           num(x);
           if(seen1>0 && seen2>0 && seen3>0 && seen4>0 && seen5>0 && seen6>0 && seen7>0 && seen8>0 && seen9>0 && seen0>0)
           {
               out<<"Case #"<<k<<": "<<n*i<<endl;
               break;
           }
        }
        }
        k++;
    }

    return 0;
}
