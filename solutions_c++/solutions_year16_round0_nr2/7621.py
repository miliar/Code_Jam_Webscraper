#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <stdio.h>
#include <string>
using namespace std;

vector<char> const12;
int no_flip=0;
bool alltrue()
{
    for (int i=0;i<const12.size();i++)
    {    
        if (const12[i]=='-')
        return false;
    }
    return true;
}
bool allfalse()
{
    for (int i=0;i<const12.size();i++)
    {    
        if (const12[i]=='+')
        return false;
    }
    return true;
}

void flip(int consec,char opposite)
{
    for (int i=0;i<consec;i++)
        const12[i]=opposite;
}
int runner()
{
if (alltrue())
    return no_flip;
    no_flip++;
    int consec=0;
    int flag=0;
    
    if (const12[0]=='+')
    {
         for (int i=0;flag!=1;i++)
        {
            if (const12[i]=='-')
            {
                consec = i;
                flag =1;
            }
        }
        flip(consec,'-');
        runner();
    }
    else if (const12[0]=='-')
    {
        if (allfalse())
        {
            flip(const12.size(),'+');
            runner();
        }
         for (int i=0;flag!=1;i++)
        {
            if (const12[i]=='+')
            {
                consec = i;
                flag =1;
            }
        }
        flip(consec,'+');
        runner();
    }
}   
int output12(string in)
{
    for (int i=0;i<in.length();i++)
    const12.push_back(in[i]);
     int x = runner();
     return x;
}
int main(){
    int T,I=0,res;
    string string_in;
    std::cin >> T;
    while(I++ != T){
        const12.clear();
        no_flip =0;
        std::cin >> string_in;
        std::cout <<"Case #"<<I<<":  ";
        res = output12(string_in);
        cout<<res<<endl;
    }
}
