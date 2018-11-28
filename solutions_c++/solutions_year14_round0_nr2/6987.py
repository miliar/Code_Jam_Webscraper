//
//  main.cpp
//  Cookie Clicker Alpha
//
//  Created by Pritam Khan on 12/04/14.
//  Copyright (c) 2014 PK. All rights reserved.
//

#include <fstream>
#include <iomanip>
using namespace std;
double c_rate=2.0,tym=0.0;
bool farm_favour(double c,double c_rate,double f_price,double c_goal,double i_rate)
{
    double t1,t2;
    t1=(c_goal-c)/c_rate;
    t2=((f_price-c)/c_rate)+(c_goal)/(c_rate+i_rate);
    if(t2<t1)
        return true;
    return false;
}
void find_time(double f_price,double i_rate,double c_goal,double c,double c_rate)
{
    while(farm_favour(c, c_rate, f_price, c_goal, i_rate)==true)
    {
        tym+=(f_price-c)/c_rate;
        c_rate+=i_rate;
        c=0;
    }
        tym+=(c_goal-c)/c_rate;
}
int main(int argc, const char * argv[])
{
    ifstream in;
    ofstream out;
    in.open(argv[1]);
    out.open("ans.out");
    int test;
    in >> test;
    for(int t=1;t<=test;t++)
    {
        tym=0;
        double c,f,x;
        in >> c>> f>>x;
        find_time(c,f,x,0,2);
        out<<"Case #"<<t<<": "<<fixed<<setprecision(7)<<tym<<endl;
    }
    in.close();
    out.close();

    return 0;
}

