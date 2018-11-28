#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
using namespace std;

bool Palindrome(unsigned long int N)
{
    unsigned long int num=N,rev=0;
    while(num>0)
    {
        rev=rev*10+(num%10);
        num/=10;
    }
    if(N==rev)
    return 1;
    else
    return 0;
}

int noOfFandS(unsigned long int start, unsigned long int end)
{
    if(start<1)
    start=1;
    int count=0;
    unsigned int root,root1;
    root=sqrt(end);
    root1=sqrt(start);
    for(unsigned long int i=root1;i<=root;++i)
        {
            if(Palindrome(i))
            {
                if(Palindrome(i*i)&&i*i>=start)
                {
                    ++count;
                }
            }
        }
    return count;
}

int main()
{
    fstream file,file1;
    file.open("input.txt");
    file1.open("output.o");
    int T,A,B;
    file>>T;
    for(int i=0;i<T;++i)
    {
        file>>A>>B;
        file1<<"Case #"<<i+1<<": "<<noOfFandS(A,B)<<endl;
    }
    return 0;
    file.close();
    file1.close();
}
