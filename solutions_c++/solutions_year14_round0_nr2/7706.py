#include <iostream>
#include <stdio.h>
#include <cstdio>
using namespace std;
double asd(double c, double f, double x){
    double t=0;
    double i=1;
    while(true){
//        cout<<c/(2+(i-1)*f)<<" "<<t<<endl;
//        cout<<c/(2+(i-1)*f) + x/(2+i*f) <<" "<<x/(2+(i-1)*f)<<"?"<<endl;
        double resp=t+x/(2+(i-1)*f);
        if(c/(2+(i-1)*f) + x/(2+i*f) >= x/(2+(i-1)*f))
            return resp;
        t+=c/(2+(i-1)*f);
        i++;

    }
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin>>t;
    for(int k=1;k<=t;k++){
        double c,f,x;
        cin>>c>>f>>x;

        printf("Case #%d: %.7f\n",k , asd(c,f,x));
    }
    return 0;
}
