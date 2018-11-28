#include <cstdlib>
#include <iostream>
using namespace std;

double C=0,F=0,X=0;
double times=0, cookie=0, farm=0;
int T=0; // testcases;
double base=2;
int main(int argc, char *argv[])
{
    freopen("/tmp/B-large.in","r",stdin);
    //freopen("/tmp/input.txt","r",stdin);
    freopen("/tmp/output.txt","w",stdout);
    cin>>T;
    for(int i=0; i<T; i++){
        cin>>C>>F>>X;
        times=0; cookie=0; farm=0;
        while( X/(farm*F+base) > X/(farm*F+base+F)+C/(farm*F+base) ){
            times=times+C/(base+farm*F);
            farm=farm+1;
        }
        times=times+X/(base+farm*F);
        //cout<<times<<endl;
        printf("Case #%d: %.7f\n",i+1,times);
    }
    //system("PAUSE");
    return EXIT_SUCCESS;
}

