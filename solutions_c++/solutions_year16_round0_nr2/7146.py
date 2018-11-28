#include<iostream>
#include<stdio.h>
#include<cstdlib>
#include<fstream>

using namespace std;

int moves(string S)
{
    int mv=0;
    int c=0;
    int len = S.length();


    if(S[0]=='-'){
        for(;c<len && S[c]!='+';c++)
            {}
        mv ++; }

    while(c<len){
        for(;c<len && S[c]!='-';c++)
            {}
        if(c==len)
            {
            break;
            }
        for(;c<len && S[c]!= '+';c++)
            {}
            mv =mv+2;
    }

    return mv;
}


int main()
{
    int TC;
    string s;
ifstream fstr("B-large.in");
ofstream ostr("B-large.out");
fstr>>TC;

for(int i=1;i<=TC;i++)
{
    fstr>>s;
    ostr<<"Case #"<<i<<": "<<moves(s)<<endl;



}


system("pause");
return 0;
}
