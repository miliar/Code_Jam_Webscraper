#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in;
    in.open("A-large.in");
    ofstream out;
    out.open("A-large.out");
    unsigned testsNo;
    in>>testsNo;
    unsigned currentTest=0;
    while(currentTest++<testsNo)
    {
        unsigned currentNo;
        in>>currentNo;
        unsigned answ=0;
        out<<"Case #"<<currentTest<<": ";
        if( currentNo!=0 )
        {
            bool seenAll;
            bool seenDigit[10]={0,0,0,0,0,0,0,0,0,0};
            unsigned temp, multip=1;
            do {
                    answ=temp=currentNo*multip++;
                    while(temp) { seenDigit[temp%10]=1; temp/=10; }
                    seenAll=1;
                    for(char i=0;i<10 && seenAll==1; i++) seenAll*=seenDigit[i];
                } while(!seenAll);
            out<<answ<<endl;
        } else out<<"INSOMNIA"<<endl;
    }
    in.close();
    out.close();
}
