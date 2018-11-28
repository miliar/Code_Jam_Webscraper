/*standin ovation*/
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    char ch;
    ifstream file_read;
    ofstream file_write;
    file_read.open("input.txt");
    file_write.open("output.out");
    int test_nos,s_max,i,friends,x,j,k,counter;
    file_read>>test_nos;
//loop for n test cases
for(i=0; i<test_nos;i++)
{
file_read>>s_max;
friends = 0;
counter =0;
file_read.get(ch);
file_read.get(ch);

x=ch -'1' + 1;
if(x==0)
{
    friends++;
    counter++;
}
else
{
    counter+=x;
}
for(j=1;j<=s_max;j++)
{
file_read.get(ch);
x=ch -'1' + 1;
if(counter<j)
{
    friends=friends+(j-counter);
    counter=counter+x+1;
}
else
{
counter+=x;
}
}
file_write<<"Case #"<<i+1<<": "<<friends<<"\n";
}
return 0;
}
