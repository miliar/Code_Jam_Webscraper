#include<iostream>
#include<conio.h>
using namespace std;
#define pi 3.14;
int main()
{
    int r1,te,inc=0,T;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("outa.in","w",stdout);
    cin>>T;
    for(int p=0;p<T;p++){inc=0;
    cin>>r1;
    cin>>te;
    for(int kk=0;;kk=kk+2)
    {
          if(te>= (((r1+kk+1)*(r1+kk+1))-((r1+kk)*(r1+kk)) ) )
          te=te-( ((r1+kk+1)*(r1+kk+1))- ((r1+kk)*(r1+kk)) );
          else
          break;
          inc++;  
    }
    cout<<"Case #"<<p+1<<": "<<inc<<endl;
    }
    //getch();
}
