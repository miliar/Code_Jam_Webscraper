#include <iostream>
#include <string>
using namespace std;

string GetDigits(unsigned long Int) //a function that returns the digits in the input
{
    if(!Int)return "0";
    string Digits;
    unsigned long power=1;
    while(Int)
    {
        Digits+=(char)(((Int/power)%10));
        Int-=((Int/power)%10)*power;
        power*=10;
    }
    return Digits;
}

int main()
{
    int T;//the number of test cases
    cin>>T;
    int N[T];
    //read all inputs
    for(int i=0; i<T; i++)
        cin>>N[i];
    //calculate and print all outputs
    for(int x=0; x<T; x++)
    {
        cout<<"\nCase #"<<x+1<<": ";
        if(!N[x])cout<<"INSOMNIA";
        else
        {
            unsigned long N2=N[x];
            bool Digits[10]= {0,0,0,0,0,0,0,0,0,0};
            while(N2<10000000)
            {
                //read N2
                string Str=GetDigits(N2);
                for(int i=0; i<Str.size(); i++)Digits[Str[i]]=1;
                //Check all digits
                bool End=1;
                for(int i=0; i<10; i++)if(!Digits[i]) End=0;
                if(End)break;
                else
                {
                    N2+=N[x];
                }
            }
            cout<<N2;
        }
    }
    cin.get();
    cin.get();
    cin.get();
}
