#include<iostream>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("asmall.txt","w",stdout);
    int t;
    cin>>t;
    int a=1;
    while(t--)
    {
              int r,t,count=0;
              cin>>r>>t;
              int x=((r+1)*(r+1))-(r*r);
              int i=1;
              while(x<=t)
              {
                        i=i+2;
                        count++;
                        t=t-x;
                        x=((r+i)*(r+i))-((r+i-1)*(r+i-1));
                        
              }
              printf("Case #%d: %d\n",a,count);
              a++;
    }
    return 0;
}
