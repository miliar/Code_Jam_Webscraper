#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;
double c=0,f=0,x=0,t=0,d=2,i=0;

double time()
{


    cin>>c>>f>>x;
    while(i+1){
    if(x/(2+f*i) > (x/(2+f*(i+1)))+ c/(2+f*i))
    {

        d = 2+(f*i);
        t = t + c/d;
       // cout<<"c/c is:"<<c/d<<endl;

       // cout<<"t is:"<<t<<endl;

    }
    else
    {
        i++;
        break;
    }
    i++;
    }
   // cout<<"i is:"<<i<<endl;
    t = t + x/(2+f*(i-1));
    //cout<<std::setprecision(10)<<t<<endl;
    return t;
}





int main()
{

     ofstream outputfile("output2.txt");
    int test=0, count=0;
    double t1 = 0;
    cin>>test;
    while(test>count)
    {
        c=0;f=0;x=0;t=0;d=2;i=0;
        t1 = time();
        outputfile<<std::setprecision(9)<<"Case #"<<count+1<<": "<<t1<<endl;
        count++;
    }

}
