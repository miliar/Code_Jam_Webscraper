#include<iostream>
#include<fstream>
#include <iomanip>
using namespace std;


int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");
    int T;
    in>>T;
    for ( int t = 0; t < T; t++)
    {
       double C, F , X;
       double bestTime;
       in>>C>>F>>X;

       double time1 = X/2;
       if ( X<=C)
            bestTime = time1;
       else
        {
            int i =1;
            while (true)
            {
                double regre= 0.0;
                for (int j = 1; j <=i; j++)
                    regre +=((C)/ (2+F*(j-1)));

                double time2 = regre+ X/(F*i+2);
                if ( time1 <= time2)
                {
                    bestTime = time1;
                    break;
                }
                else
                {
                    time1 = time2;

                }
                i++;
            }
        }
       out<<"Case #"<<t+1<<": ";
       out<<fixed;
       out.precision(7);
       out<<bestTime<<endl;

    }
    in.close();out.close();
}
