#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    std::cout.precision(30);
    int t;
    cin>>t;
    for(int i1=1;i1<=t;i1++)
    {
       double c,f,x,a[100005]={0},res=0,ans1=0;
       int n=1;
       cin>>c>>f>>x;
       a[0]=x/2;
       for(double i=1,j=0;;i=i+1,j=j+1)
       {
           ans1+= c/((double)(2+j*f)) ;
           double ans2= x/ (double)(2+i*f);
           a[n] = ans1+ans2;
           if(a[1]>a[0])
           {
               res=a[0];
               break;
           }

           if(a[n]>a[n-1])
           {
               res=a[n-1];
               break;

           }
           n++;
       }
       cout<<"Case #"<<i1<<": ";
       //cout<<res<<endl;
       cout<<res<<endl;



    }
    return 0;
}
