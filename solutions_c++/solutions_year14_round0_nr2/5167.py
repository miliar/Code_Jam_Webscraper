#include<iostream>
#include<fstream>
#include <iomanip>
#include <sstream>

using namespace std;
main()
{
    ofstream outputfile("cookie2.txt");
	int counter=1,t;
    long double time=0.0,d=2,c,f,x;
    cin>>t;
    std::cout.unsetf ( std::ios::floatfield );                // floatfield not set
    std::cout.precision(10);
    while(counter!=(t+1))
    {
    	time = 0.0; d=2.0;
        cin>>c>>f>>x;
    std::cout.unsetf ( std::ios::floatfield );                // floatfield not set
    std::cout.precision(10);
        while(1)
        {
        	
    std::cout.unsetf ( std::ios::floatfield );                // floatfield not set
    std::cout.precision(10);
            if(x/d>(x/(d+f)+c/d))
            {
                time=time+c/d;
                d=d+f;
            }
            else
            {
                time=time+x/d;
                break;
            }
        }
    	outputfile<<"Case #"<< std::setprecision(10)<<counter<<": "<<time<<"\n";
    	counter++;
    }
}

