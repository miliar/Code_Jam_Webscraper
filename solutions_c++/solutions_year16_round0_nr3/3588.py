#include <iostream>
#include <string.h>
using namespace std;

unsigned long long InterpretToBase(string Jamcoin, int Base)
{
    unsigned long long Value=0, power=1;
    for(int i=Jamcoin.size()-1; i>=0; i--, power*=Base)
    {
        if(Jamcoin[i]=='1')Value+=power;
    }
    return Value;
}

int Divisor(unsigned long long Value) //a function that returns zero if the input is prime. Else it returns the smallest divisor
{
    for(int divisor=2; divisor<Value; divisor++)
    {
        if(!(Value%divisor))return divisor;
        if(divisor>1024)return 0; //this condition is only added to save processing time by ignoring jamconis that have large non-trivial divisors
    }
    return 0;
}

int main()
{
    int T;//the number of test cases
    cin>>T;
    int N[T], J[T];
    //read all inputs
    for(int i=0; i<T; i++)
        cin>>N[i]>>J[i];
    //calculate and print all outputs
    for(int x=0; x<T; x++)
    {
        cout<<"\n\nCase #"<<x+1<<":";
        /***find all jamcoins***/
            //Set default value to a loop variable
            string TempJC="1";
            for(int i=0;i<N[x]-2; i++)TempJC+="0";
            TempJC+="1";
            //loop to see all possible binary values
            int NumberOfJamsFound=0;
            string MaxV;
            for(int i=0; i<N[x]; i++)MaxV+="1";
            while(1)
            {
                //see if the current value is a jamcoin
                bool IsJam=1;
                for(int i=2; i<=10; i++)
                {
                    if(!Divisor(InterpretToBase(TempJC,i)))IsJam=0;
                }
                if(IsJam)
                {
                    //print the jamcoin
                    cout<<"\n"<<TempJC;
                    for(int i=2; i<=10; i++)cout<<" "<<Divisor(InterpretToBase(TempJC, i));
                    NumberOfJamsFound++;
                    if(NumberOfJamsFound==J[x])break;
                }
                //increment the binary value
                if(TempJC==MaxV)break;
                for(int i=N[x]-2; i>0; i--)
                {
                    if(TempJC[i]=='0')
                    {
                        TempJC[i]='1';
                        for(int ii=N[x]-2; ii>i; ii--)TempJC[ii]='0';
                        break;
                    }
                }
            }
    }
    cin.get();
    cin.get();
    cin.get();
}
