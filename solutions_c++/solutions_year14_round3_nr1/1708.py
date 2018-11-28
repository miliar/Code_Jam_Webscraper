#include<iostream>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<fstream>

using namespace std;

int main()
{
    int P,Q,T,i,x,y;
    double k;
    string read,num;
    fstream input;
    fstream output;
    input.open("A-small.txt",ios::in);
    output.open("A-small-out.txt",ios::out);
    input>>T;
    for (x=1;x<=T;x++)
    {
        input>>read;
        num.clear();
        for (i=0;read[i]!='/';i++)
            num += read[i];
        P = atoi(num.c_str());
        num.clear();
        for (i=i+1;read[i]!='\0';i++)
            num += read[i];
        Q = atoi(num.c_str());
        k = (double)P/Q;
        for (y=0;k<1.0;y++)
            k = k*2.0;
        while ((Q%2 )==0)
            Q = Q/2;
        if (Q==1)
            output<<"Case #"<<x<<": "<<y<<endl;
        else
            output<<"Case #"<<x<<": impossible"<<endl;
    }
    input.close();
    output.close();
    return 0;
}
