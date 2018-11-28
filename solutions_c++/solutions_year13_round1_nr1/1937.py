#include<iostream>
#include<conio.h>
using namespace std;
#define pi 3.14;
int main()
{
    int r,t,count=0,T;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("outl.in","w",stdout);
    cin>>T;
    for(int j=0;j<T;j++){count=0;
    cin>>r;
    cin>>t;
    for(int i=0;;i=i+2)
    {
          //cout<<((r+i+1)*(r+i+1))-((r+i)*(r+i)) ;
          if(t>= (((r+i+1)*(r+i+1))-((r+i)*(r+i)) ) )
          t=t-( ((r+i+1)*(r+i+1))- ((r+i)*(r+i)) );
          else
          break;
          count++;  
    }
    cout<<"Case #"<<j+1<<": "<<count<<endl;
    }
    getch();
}
