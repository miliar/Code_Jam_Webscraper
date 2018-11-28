#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;

int main()
{
    ifstream input("B-large.in");
    ofstream output("output_00l.txt");
    int N,counter=0,i,repeats=0;
    char c,flip;
    input>> N;
    input.get(c);
    for(i=0;i<N;i++)
    {
        output<<"Case #"<<i+1<<": ";
        input.get(c);
        flip=c;
        do
        {
            input.get(c);
            if((flip!=c) &&(c!='\n'))
                {
                  if(flip=='-')
                  {
                        counter++;
                        flip='+';
                  }
                    else
                    {
                        counter++;
                        flip='-';
                    }
                }
            repeats++;
        }while(c!='\n');
        if(flip=='-')
        {
            counter++;
        }
        output<<counter<<endl;
        counter=0;
        repeats=0;
    }
    input.close();
    output.close();
    return 0;
}
