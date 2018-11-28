#include <iostream>
#include <cstdio>
#include <cstring>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <ctime>
#include <cstring>
#include <sstream>
#include <fstream>
using namespace std;
double solver(double c,double f,double x)
{
    double speed=2.0, temp1=x/speed, temp2=0.0;
    while(1){
            temp2+=c/speed;
            speed+=f;
            temp2+=x/speed;
            if(temp1<temp2)
                return temp1;
            else{
                temp1=temp2;
                temp2=temp2-x/speed;
            }
    }
    
}
int main( )
{   
    /*clock_t start;
    start=clock();
    /***********************************************/
    freopen("B-large.in", "rt", stdin);
    freopen("B-large.out", "wt", stdout);
    int t;
    cin>>t;
    for(int i=1; i<t+1; ++i) {
        cout<<"Case #"<<i<<": ";
        double c, f, x;
        cin>>c>>f>>x;
        printf("%.7lf\n", solver(c, f, x) );
    }
    /************************************************
    start=clock()-start;
    printf("Time = %f\n", (float)start/CLOCKS_PER_SEC);*/
    return 0 ;
}