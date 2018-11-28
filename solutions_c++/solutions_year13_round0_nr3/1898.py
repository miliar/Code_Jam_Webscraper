#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
using namespace std;

unsigned long long last_square;

bool isFair(unsigned long long i)
{
    int b[100];
    int counter = 0;
    bool condition = true;

    while(i)
    {
        b[++counter] = (i % 10);
        i /= 10;
    }

    if( counter % 2 )
        for(int i = 0; i <= (counter/2); i++)
            if( b[(counter/2) + 1 + i] != b[(counter/2) + 1 - i] )
                condition = false;
    if( !(counter % 2) )
        for(int i=0; i < (counter)/2; i++ )
            if( b[(counter/2) - i] != b[ (counter/2) + 1 + i ] )
                condition = false;

    return condition;

}

bool isSquare(unsigned long long x)
{
    for(unsigned long long i = last_square; i < x/2; i++ )
        if( (i*i) == x )
            return true;
    return false;
}

int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("output.out","w",stdout);

    // generate the fair and square numbers
    unsigned long long a[1000];
    a[0]=0; a[1]=1; a[2] = 4;
    int counter = 3;
    for(unsigned long long i = 3; i <= 10000000; i++)
        if( isFair(i*i) && isFair(i) )
        {
            a[counter++] = i*i;
        }

    int T;
    unsigned long long n;
    unsigned long long m;
    scanf("%d",&T);

    for(int i=1; i<=T; i++)
    {
        scanf("%llu%llu",&n,&m);
        int counter2=0;
        for(int j = 0; (j<counter) && (a[j] <= m); j++)
            if( (a[j] >= n) )
                counter2++;

        cout<<"Case #"<<i<<": "<<counter2<<'\n';

    }
/*
    for(int i=0; i<counter; i++)
        printf("%llu\n",a[i]);
*/
    return 0;
}

