#include <iostream>
#include <iomanip>

using namespace std;
int main()
{
    double C,F,X,R=2.0,keep=0.0;
    double time1=0.0,time2=0.0,temp=0.0;
    int flag=0,run,test;
    cin>>test;
    for(run=1;run<=test;run++)
    {
    keep=0,time1=0.0,time2=0.0;
    flag=0;
    R=2.0;
    cin>>C>>F>>X;
    while(flag!=1)
    {
        time1=X/R+keep;
        temp=C/R;
        time2=X/(R+F)+temp+keep;
        if(time1<time2)
        {
        flag=1;
        cout<<"Case #"<<run<<": "<<std::fixed<<std::setprecision(7)<<time1<<endl;
        }
        keep=C/R+keep;
        R=R+F;
    }
    }
    return 0;
}
