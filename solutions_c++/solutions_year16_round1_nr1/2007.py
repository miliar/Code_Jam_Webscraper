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
        OutputBuffer+="\nCase #"+IntToStr(x+1)+": ";
        string S;
        cin>>S;
        string LastWord;
        LastWord+=S[0];
        for(unsigned i=1; i<S.size(); i++)
        {
            string temp;
            temp+=S[i];
            if(LastWord[0]<=S[i])
                LastWord=temp+LastWord;
            else
                LastWord+=temp;
        }
        OutputBuffer+=LastWord;
    }
    cout<<OutputBuffer;
    cin.get();
    cin.get();
    cin.get();
}
