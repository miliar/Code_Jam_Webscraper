#include<fstream>
#include<iostream>
using namespace std;

#define IN_FILE "blue.in"
#define OUT_FILE "output.txt"

int main()
{
    ofstream out;
    ifstream in;
    out.open(OUT_FILE);
    in.open(IN_FILE);
    out.precision(8);
    out.setf(ios::fixed);
    int t;
    in>>t;
    cout<<t;
    for(int no=1;no<=t;++no)
    {
        double c,f,time,present_min,rate,money,x;
        in>>c>>f>>x;
        /*
            You either don't buy till the end of time
            or you buy at the first chance you get
        */
        time = 0;money = 0;rate = 2;
        present_min = x/2;
        while(time < present_min)
        {
            //alrdy done
            if(money>=x)
            {
                present_min = min(present_min,time);
                break;
            }
            //Do not buy
            present_min = min(present_min,time + (x-money)/rate);
            //Buy
            double extra_time = (c - money)/rate;
            money+= extra_time*rate - c;
            rate+=f;
            time+=extra_time;
        }
        out<<"Case #"<<no<<": "<<present_min<<'\n';
        //cout<<"Case #"<<no<<": "<<present_min<<'\n';
    }
    out.close();
    in.close();
    return 0;
}
