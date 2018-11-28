#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
    std::ifstream myfile("B-large.in");
    std::ofstream myfile2("output.txt");
    int t;
    myfile>> t;
    for(int i=0;i<t;i++)
    {
        double c,f,x,r=2;
        myfile>> c;
        myfile>> f;
        myfile>> x;
        long double time=0,time2=0,time3=0;
        double cookie;
        if(x<c)
        {
            time= x/r;
        }
        else
        {
        time= (c/r);
        cookie= x-c;
        while(cookie)
        {
            time2= ((cookie)/r);
            time3= ((cookie+c)/(r+f));
            if(time2<time3)
            {
                if(cookie>=c)
                {
                    time= time+ (c/r);
                    cookie-= c;
                }
                else
                {
                    time= time+ time2;
                    cookie=0;
                }
            }
            else
            {
                    r= r+f;
                    time= time+ (c/r);
            }
        }
        }
        myfile2<<"Case #"<<(i+1)<<": ";
        myfile2<<setprecision(7)<<fixed;
        myfile2<<time<<"\n";
    }
    myfile.close();
    myfile2.close();
    return 0;
}
