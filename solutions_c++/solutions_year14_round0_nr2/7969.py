#include <iostream>
#include <iomanip>

int main()
{
    int T;
    std::cin >> T;
    for(int i = 0; i<T; i++)
    {
        double C, F, X;
        std::cin>>C>>F>>X;
        double nCookies = 0;        
        double r = 2;
        double totTime = 0;
        bool done = false;
        while(!done){
            double timeXwC = C/r + X/(r+F);
            double timeXwoC = X/r;
            if(timeXwC < timeXwoC)
            {
                totTime += C/r;
                r += F;
            }
            else
            {
                totTime += timeXwoC;
                done = true;
            }
        }
        std::cout<<"Case #"<<i+1<<": "<<std::setprecision(7)<<std::fixed<<totTime<<std::endl;
    }
}
