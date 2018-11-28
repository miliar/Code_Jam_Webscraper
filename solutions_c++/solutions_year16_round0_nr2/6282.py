#include<iostream>
#include<fstream>
#include<vector>

using namespace std;
int main()
{
ifstream in("B-large.in");
ofstream out("output.txt");

string v;
long test ;
in>>test;

long mov = 0 ;
for(long j=1;j<=test ; j++)
{
    mov = 0;
    in>>v;

    for(long i = 0 ; i<v.length(); i++)
    {
        if(i == (v.length()-1) && v[i]=='-')
            mov++;
        if(i>0 && v[i-1]=='+' && v[i]=='-')
            mov++;
        if(i>0 && v[i-1]=='-' && v[i]=='+')
            mov++;

    }

    out<<"Case #"<<j <<": "<<mov<<endl;

}


return 0 ;
}
