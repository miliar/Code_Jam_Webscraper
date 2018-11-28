#include<iostream>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
using namespace std;

char buffer[1000];

void print_mid(int n, int total)
{
    if(n % 2)
    {
        buffer[n/2] = '1';
        cout<<buffer<<endl;
        buffer[n/2] = '0';

        if(total <= 4)
        {
            buffer[n/2] = '2';
            cout<<buffer<<endl;
            buffer[n/2] = '0';
        }
    }
}

void re_generate(int beg, int end, int n, int total)
{
    if(total == 8)
        return;

    if(beg > end)
        return;

    if(beg == end)
    {
        buffer[beg] = buffer[n - beg - 1] = '1';
        cout<<buffer<<endl;
        print_mid(n, total + 2);
        buffer[beg] = buffer[n - beg - 1] = '0';
        return;
    }


    for(int i = beg; i <= end; ++i)
    {
        buffer[i] = buffer[n - i - 1] = '1';
        cout<<buffer<<endl;
        print_mid(n, total + 2);
        re_generate(i + 1, end, n, total+2);
        buffer[i] = buffer[n - i - 1] = '0'; 
    }
    
}


void generate(int n)
{
    
    buffer[n] = '\0';

    for(int i = 0; i < n; ++i)
        buffer[i] = '0';

    buffer[0] = '1';
    buffer[n - 1] = '1';
    
    int end = n / 2 - 1;
   cout<<buffer<<endl; 
   print_mid(n, 2);
   re_generate(1, end, n, 2);
}

void generate2(int n)
{

    buffer[n] = '\0';
    for(int i = 0; i < n; ++i)
        buffer[i] = '0';

    buffer[0] = '2';
    buffer[n - 1] = '2';
    cout<<buffer<<endl;
    if(n % 2)
    {    
        buffer[n/2] = '1';
        cout<<buffer<<endl;
    }
}

int main(int argc, char* argv[])
{
    int num = 6;
    if(argc > 1)
        sscanf(argv[1], "%d", &num);
    
    cout<<1<<endl; 
    cout<<2<<endl; 
    cout<<3<<endl; 

    for(int i = 2; i <= 50; ++i)
    {
        generate(i);
        generate2(i);
    }

    return 0;
}


