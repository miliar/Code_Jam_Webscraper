#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int test;
    double c,f,x,min,ctime,time,t;
    cin>>test;
    int i=1;
    while(i<=test){
        cin>>c>>f>>x;
        t=2; time=0.0;
        min=double(x/t);
        ctime=c/t;
        t=t+f;
        time=ctime+double(x/t);
        while(time<min){
            min=time;
            ctime+=double(c/t);
            t=t+f;
            time=ctime+double(x/t);
        }
        printf("Case #%d: %.7lf",i,min);
        cout<<endl;
        i++;
    }
    return 0;
}
