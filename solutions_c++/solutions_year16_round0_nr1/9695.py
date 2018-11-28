#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include <fstream>

using namespace std;

int main()
{
ifstream input; //Creating object for input stream
ofstream output; //Creating object for output stream

input.open("A-large.in");    //open a file to read input
output.open("outlg.txt"); //open a file to write output
int test,number,loop,counts,temp_number,i,digit;
bool hsh[10];
input>>test;
for(loop=1;loop<=test;loop++)
{
input>>number;
memset(hsh,false,sizeof hsh);
counts=0;
if(number!=0)
{
for(i=1;counts!=10;i++)
{
temp_number=number*i;
do
{
digit=temp_number%10;
if(!hsh[digit])
{
hsh[digit]=true;
counts++;
}
temp_number/=10;
}
while(temp_number>0&&counts!=10);
}
output<<"Case #"<<loop<<": "<<(number*(i-1))<<endl;
}
else
output<<"Case #"<<loop<<": "<<"INSOMNIA"<<endl;
}
input.close();             //closing the input file
output.close();            //closing the output file
return 0;
}
