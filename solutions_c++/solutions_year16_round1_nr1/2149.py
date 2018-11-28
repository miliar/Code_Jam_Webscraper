#include<cstdio>
#include<iostream>
#include<algorithm>
#include <fstream>
#include<cstring>
#include<algorithm>
#include<string>

using namespace std;

int main()
{
    ifstream in; //Creating object for input stream
    ofstream out; //Creating object for output stream
    in.open("input.in");    //open a file to read input
    out.open("outlarge.txt"); //open a file to write output
    int test,loop,len,i;
    string s,as;
    in>>test;
    for(loop=1;loop<=test;loop++)
    {
        in>>s;
        len=s.length();
        as=as+s[0];
        for(i=1;i<len;i++)
        {
            if(s[i]>=as[0])
                as=s[i]+as;
            else
                as=as+s[i];
        }
        out<<"Case #"<<loop<<": "<<as<<endl;
        as.clear();
    }
    in.close();             //closing the input file
    out.close();            //closing the output file
return 0;
}
