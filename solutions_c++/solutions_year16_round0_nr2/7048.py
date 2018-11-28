#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int T;
    cin>>T;
    cin.ignore(256,'\n');
    for(int jj=1; jj<=T; ++jj)
    {
        char ch;
        ch = getchar();
        char prev = ch;
        long int counter = 0;
        while(ch != '\n')
        {
            if(prev != ch)
            {
                counter ++;
                prev = ch;
            }
            ch = getchar();
        }
        ch = '+';
        if(prev != ch)
        {
            counter ++;
            prev = ch;
        }
        cout<<"\nCase #"<<jj<<": "<<counter;
    }
    return 0;
}
