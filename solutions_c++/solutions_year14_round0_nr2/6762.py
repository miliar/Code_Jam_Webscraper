#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    cout.precision(10);
    for(int i=0;i<t;i++)
    {
        long double c, f, x;
        cin>>c>>f>>x;
        long double time=0;
        long double speed=2.0;
        while(((x-c)/speed)>(x/(speed+f))){
            time = time + c/speed;
            //cout<<time<<endl;
            speed+=f;
           // cout<<time<<" "<<speed<<endl;
            }
        time=time+((x)/speed);
        cout<<"Case #"<<i+1<<": "<<time<<endl;
    }
    return 0;
}
