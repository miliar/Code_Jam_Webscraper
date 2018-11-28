#include <iostream>
#include <fstream>
using namespace std;
long long int power(long long int k,long long int c)
{
    long long int sum=1;
    for(int i=1;i<=c;i++)
    {
        sum*=k;
    }
    return sum;
}
int main()
{
    ofstream out("out.txt");
    ifstream in("in.txt");
    int test;
    in>>test;
    for(int t=1;t<=test;t++)
    {
        long long int k,c,s;
        in>>k>>c>>s;
        long long int x=power(k,c-1);
        long long int sum=1;
        out<< "Case #"<<t<< ": "<<sum<< " ";
        for(int i=1;i<k;i++)
        {
            out<<(sum+x)<< " ";
            sum+=x;
        }
        out<<endl;
    }
    return 0;
}
