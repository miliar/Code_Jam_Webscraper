#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cstdio>

using namespace std;

int main(int argc, const char * argv[])
{

    int T;
    double C,F,X;
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        cin>>C>>F>>X;
        double opt=X*1.0/2.0,A=0,FF=0;
        while(A<opt){
            A+=C/(2+FF);
            double c_opt=A+X*1.0/(2+FF+F);
            FF+=(double)F;
            opt=min(opt,c_opt);
        }
        cout<<"Case #"<<cas<<": ";
        printf("%.7lf\n",opt);
    }
    return 0;
}

