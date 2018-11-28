#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

bool is_palindrome(int i)
{
    int reverse=0;
    int n=i;
    while(n>0)
    {
        int digit=(n%10);
        reverse*=10;
        reverse+=digit;
        n/=10;
    }
    return (i==reverse);
}

int is_square(int i)
{
    int j=sqrt(i);
    int k=pow(j,2);
    if(i==k)
    {
        return j;
    }
    else
    {
        return 0;
    }
}

int main()
{
    ifstream fin;
    fin.open("in.txt",ios::in);
    ofstream fout;
    fout.open("out.txt",ios::out|ios::trunc);
    int t;
    fin>>t;
    for(int i=0;i<t;i++)
    {
        int low,high;
        fin>>low>>high;
        int count=0;
        bool fair_and_square;
        for(int j=low;j<=high;j++)
        {
            fair_and_square=false;
            if(is_palindrome(j))
            {
                int k=is_square(j);
                if(k>0)
                {
                    if(is_palindrome(k))
                    {
                        fair_and_square=true;
                    }
                }
            }
            if(fair_and_square)
            {
                count++;
            }
        }
        fout<<"Case #"<<(i+1)<<": "<<count<<endl;
    }
    return 0;
}
