#include <iostream>
#include <fstream>
using namespace std;

long long int*a,n;

int min(long long int a, long long int b)
{
    if(a>b)
    {
        return b;
    }
    return a;
}
long long int findSug()
{
    long long int max = 0;
    for(long long int i=1; i<n; i++)
    {
        if(a[i-1]-a[i]>max)
        {
            max = a[i-1]-a[i];
        }
    }
    return max;
}
long long int c1()
{
    long long int count = 0;
    for(long long int i=1; i<n; i++)
    {

        if(a[i]<a[i-1])
        {
            count+=(a[i-1]-a[i]);
        }
        else
        {

        }
    }
    return count;
}
long long int c2()
{
    long long int count = 0, sug = findSug();
    for(long long int i=1; i<n; i++)
    {
        count+=min(a[i-1],sug);

    }
    return count;
}
int main()
{
    long long int T,a1,a2;
    ifstream in;
    in.open("A-large (1).in");
    ofstream out;
    out.open("out.txt");
    in>>T;
    for(long long int t=1; t<=T; t++)
    {
        in>>n;
        a = new long long int[n];
        for(int i=0; i<n; i++)
        {
            in>>a[i];
        }
        a1 = c1();
        a2 = c2();
        out<<"Case #"<<t<<": "<<a1<<" "<<a2<<endl;
    }
    return 0;
}
