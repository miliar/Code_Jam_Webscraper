#include<iostream>
#include<cstdio>
#include<cstdlib>
//#define MYDEBUG
#define RANGE 100000000000000ll
#define TABLESIZE 39
using namespace std;

long long int table[TABLESIZE];
int len;

bool checkP(long long int n)
{
    int stackn[20];
    int len=0;
    while(n>0)
    {
        stackn[len++]=n%10;
        n/=10;
    }

    for(int i=0; i<len/2; i++)
        if(stackn[i]!=stackn[len-1-i])
            return false;

    return true;
}


void maketable()
{
    long long int i=1;
        for(;i*i<=RANGE;i++)
        {
            if(checkP(i)&&checkP(i*i))
            {
                table[len++]=i*i;
            }
        }
    #ifdef MYDEBUG

    printf("table");
    for(int j=0; j<len; j++)
    {
        cout << table[j] <<endl;
    }

    #endif
}


int main()
{
    freopen("C.in.txt","r",stdin);
    freopen("C.out.txt","w",stdout);

    maketable();

    int T;

    cin >> T;


    int r=0;
    while(r<T)
    {
        r++;
        long long int a,b;
        int counting = 0;
        cin >> a >> b;
        int s;
        for(s=0; table[s]<a;s++);
        for(;table[s]<=b&&s<len;s++)
            counting++;


        printf("Case #%d: %d\n",r,counting);
    }

}
