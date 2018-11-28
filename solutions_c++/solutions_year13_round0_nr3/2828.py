#include<strings.h>
#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int ts,z=0;
    ifstream cinner("C-small-attempt0.in",ios::in);
    cinner>>ts;
    ofstream coutter("out.txt",ios::out);
    for(; z<ts; z++)
    {
        int a,b,out=0;
        //1,4,9,121,484
        cinner>>a>>b;

        if(a<=1)out+=5;
        else if(a<=4)out+=4;
        else if(a<=9)out+=3;
        else if(a<=121)out+=2;
        else if(a<=484)out+=1;
        else out+=0;

        if(b>=484)out-=0;
        else if(b>=121)out-=1;
        else if(b>=9)out-=2;
        else if(b>=4)out-=3;
        else if(b>=1)out-=4;

        coutter<<"Case #"<<z+1<<": "<<out<<"\n";

    }
    return 0;
}

