#include <iostream>
#include <string.h>
using namespace std;

string IntToStr(long Int)
{
    if(!Int)return "0";
    string Str;
    bool negative=0;
    if(Int<0)
    {
        negative=1;
        Int*=-1;
    }
    unsigned long power=1;
    while(Int)
    {
        Str+=(char)(((Int/power)%10)+48);
        Int-=((Int/power)%10)*power;
        power*=10;
    }
    if(negative) Str+="-";

    string s2;
    for(int x=(Str.size()-1); x>=0; x--)//revers the order of all characters
    {
        s2+=Str[x];
    }
    return s2;
}

int main()
{
    string OutputBuffer="\n";
    unsigned T;
    cin>>T;
    for(int x=0; x<T; x++)
    {
        unsigned N;
        cin>>N;
        OutputBuffer+="\nCase #"+IntToStr(x+1)+":";
        unsigned L[2*N-1][N];
        unsigned MissingList[N];
        unsigned MissingListIndex=0;
        for(unsigned Y=0; Y<2*N-1; Y++)
        {
            for(unsigned X=0; X<N; X++)
            {
                cin>>L[Y][X];
            }
        }
        for(unsigned Y=0; Y<2*N-1; Y++)
        {
            for(unsigned X=0; X<N; X++)
            {
                bool recorded=0;
                for(unsigned i=0; i<MissingListIndex; i++)
                    if(MissingList[i]==L[Y][X]) recorded=1;
                if(!recorded)
                {
                    unsigned Nx=0;
                    for(unsigned Y2=0; Y2<2*N-1; Y2++)
                    {
                        for(unsigned X2=0; X2<N; X2++)
                        {
                            if(L[Y][X]==L[Y2][X2])Nx++;
                        }
                    }
                    if(Nx%2)
                    {
                        MissingList[MissingListIndex]=L[Y][X];
                        MissingListIndex++;
                    }
                }
            }
        }
        //Arrange
        unsigned MaxPrinted=0;
        for(unsigned i=0; i<MissingListIndex; i++)
        {
            unsigned Min=3000;
            for(unsigned ii=0; ii<MissingListIndex; ii++)
            {
                if(MissingList[ii]>MaxPrinted&&MissingList[ii]<Min)Min=MissingList[ii];
            }
            OutputBuffer+=" "+IntToStr(Min);
            MaxPrinted=Min;
        }
    }
    cout<<OutputBuffer;
    cin.get();
    cin.get();
    cin.get();
}
