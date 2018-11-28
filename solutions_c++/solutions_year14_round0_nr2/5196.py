#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
    int t;
    cin>>t;
    setprecision(8);
    for(int i=0;i<t;i++)
    {
        long double c, f, x;
        cin>>c>>f>>x;
        long double time=0.0;
        long double speed=2.0;
        while(((x-c)/speed)>(x/(speed+f)))
		{
            time = time + c/speed;
            speed+=f;
        }
        time=time+((x)/speed);
        cout<<"Case #"<<i+1<<": "<<fixed<<time<<endl;
    }
    return 0;
}

