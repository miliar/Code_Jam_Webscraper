#include <iostream>
#include<fstream>
#include<stdio.h>
using namespace std;

ifstream in("test.txt", ios::in);
ofstream out("result2.txt", ios::out);

int calc(unsigned int A , unsigned int B ,unsigned int K);

int main()
{
    unsigned int T , i = 0 , j = 0 , A = 0 , B = 0 , K = 0;
        in>>T;
        for(i = 0 ; i < T ; i++)
        {
         in>>A;
         in>>B;
         in>>K ;
         //cout<<A<<B<<K;
                  cout<<calc(A,B,K);
                  out<<"Case #"<<i+1<<": "<<calc(A,B,K)<<"\n";
        cout<<"\n";
        }

    return 0;
}


int calc(unsigned int A ,unsigned int B ,unsigned int K)
{
    unsigned int i = 0 , j = 0 ,C = 0 , l = 0 , count = 0;
    for(i = 0 ; i < A ; i++)
    {
        for(j = 0 ; j < B ; j++)
        {
            C = i&j;
            if(C < K)
                count++;

        }
    }
    return count;
}
