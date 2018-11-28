#include <iostream>
#include <fstream>

using namespace std;

bool isVisited(long array[]);

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("outputLarge.out");

    long numCase; //number of test cases
    long i; //loop counter

    fin >> numCase; //input number of cases
    long N,temp,mul=1,rem;
    long array[10];
    int j;

    for(i = 1;i<=numCase;i++)
    {
        mul=1;
        for(j=0;j<10;j++)
        {
            array[j] = 0;
        }
        fin>>N;
        if(N==0)
        {
            fout << "Case #" << i << ": " <<"INSOMNIA"<<endl; //endless
        }
        else
        {
            while(!isVisited(array))
            {
                temp = N*mul;
                while(temp!=0)
                {
                    rem = temp%10;
                    temp = temp/10;
                    array[rem] = 1;
                }
                mul++;
            }
            fout << "Case #" << i << ": " <<(N*(mul-1))<<endl;
        }
    }
    return 0;
}

bool isVisited(long array[])
{
    int n = 0, ct=0;
    while(n<10)
    {
        if(array[n]==1)
        {
            ct = ct +1;
        }
        n++;
    }
    if(ct == 10)
    {
        return true;
    }
    else
    {
        return false;
    }
}
