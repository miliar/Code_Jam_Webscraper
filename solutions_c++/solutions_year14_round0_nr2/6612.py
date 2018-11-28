#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;

int main()
{
    int testCases,count=0,flag;
    double C,F,X,sec,sec1,sec2;
    ifstream myfileInput;
    ofstream myfileOutput;
    myfileInput.open("input.txt");
    myfileOutput.open("output.txt");
    myfileInput>>testCases;
    while(testCases>0)
    {
        count++;
        myfileInput>>C>>F>>X;
        sec=C/2;
        sec1=X/2;
        sec2= sec+X/(2+F);
        sec=sec+C/(2+F);
        flag=2;
        while(1)
        {
            if(sec1<=sec2)
            {
                myfileOutput<<std::fixed;
                myfileOutput<<std::setprecision(7)<<"Case #"<<count<<": "<<sec1<<"\n";
                break;
            }
            else
            {
                sec1=sec2;
                sec2=sec+X/(2+flag*F);
                sec= sec+ C/(2+flag*F);
                flag++;
            }
        }
        testCases--;
    }
}
