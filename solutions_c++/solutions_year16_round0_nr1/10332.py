#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;
#define maximum 99999999
bool trackdigits[10];

void resetbool()
{
    for(int i=0; i<10; i++)
    {
        trackdigits[i]=false;
    }
}

bool isboolcomplete()
{
    for(int i=0; i<10; i++)
    {
        if(trackdigits[i]==false)
            return false;
    }
    return true;
}

int main()
{
    ofstream fout;
    fout.open("output-large.txt");
    ifstream fin;

    fin.open("A-large.in");
    int t;
    fin>>t;
    int multiple,n,givennumber,number,currentnumber;
    bool notdone;
    int digit;
    for(int k=1; k<=t; k++)
    {
        notdone=true;
        resetbool();
        fin>>givennumber;
        multiple=1;
        while(multiple < maximum)
        {
            currentnumber= givennumber * multiple;
            number=currentnumber;
            while (number > 0)
            {
                digit = number%10;
                number /= 10;
                trackdigits[digit]=true;
            }
            if(isboolcomplete())
            {
                cout<<"Case #"<<k<<": "<<currentnumber<<endl;
                fout<<"Case #"<<k<<": "<<currentnumber<<endl;
                notdone=false;
                break;
            }
            multiple++;
        }
        if(notdone)
        {
            cout<<"Case #"<<k<<": INSOMNIA"<<endl;
            fout<<"Case #"<<k<<": INSOMNIA"<<endl;        }
    }
    fout.close();
    return 0;
}
