#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int cnt=0;
    while(t--)
    {
              cnt++;
              double c,f,x,r=2.0,time=0.0;
              cin>>c>>f>>x;
              int flag=1;
              while(flag==1)
              {
                  time+=c/r;
                  if((x-c)/r>=x/(r+f))
                  {
                                      r=r+f;
                  }
                  else
                  {
                      time+=(x-c)/r;
                      flag=0;
                  }
              }
              cout<<"Case #"<<cnt<<": ";
              cout.setf(ios::fixed,ios::floatfield);
              cout.precision(7);
              cout<<time<<endl;
    }
    return 0;
}
