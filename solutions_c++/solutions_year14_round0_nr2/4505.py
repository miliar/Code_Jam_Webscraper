#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;
int main()
{
    int t;
    cin>>t;
    double speed=2.0,c,f,x,time1=0,time2=0,total=0.0;
    for(int k=1;k<=t;k++)    {
    speed=2.0;
    total = 0.0;
    cin>>c;
    cin>>f;
    cin>>x;

    time2 = c/speed + x/(speed+f);
    time1 = x/speed;
    //cout<<time1<<" "<<time2;
    while(time1>time2)
    {
        total = total + c/speed;
        //cout<< time2<<" " <<total<<endl;
        speed = speed + f;
        time2 = c /speed+ x/(speed+f);
        time1 = x /speed;

    }
  total = total + time1;
  cout<<"Case #"<<(k)<<": ";
  printf("%0.7f",total);
  cout<<endl;
    }
    return 0;
}

