#include<iostream>
#include<fstream>
#include<string.h>

using namespace std;

int allnums[10];

int checkallnums()
{
    for(int i=0; i<10; i++)
    {
        if(allnums[i]== 0)
        {
            return 0;
        }
    }
    return 1;
}

void addset(int i)
{
    int a =1;
    while( i / a != 0)
    {
        int c  = (i/a) %10;
        allnums[c] = 1;
        a*=10;
    }
}

int main()
{
    ifstream fin("input.txt",ios::in);
    fstream fout("output.txt",ios::out);
    int t;
    fin>>t;
    bool flag;
    for(int c=1; c<=t; c++)
    {
        int n;
        flag=true;
        fin>>n;
        if(n==0)
        {
            flag = false;
        }
        for(int i=0; i<10; i++)
        {
            allnums[i]= 0;
        }
        int i= 1;
        while(checkallnums() ==  0 && flag == true)
        {
            addset(i*n);
            i++;
        }
        if(flag == false)
        {
            fout<<"Case #"<<c<<": INSOMNIA"<<endl;
        }
        else
        {
            fout<<"Case #"<<c<<": "<<(i-1)*n<<endl;
        }
    }
    return 0;
}
