#include <iostream>
#include <fstream>
using namespace std;
void breaknfill(bool *b,long long int n)
{
    while(n>0)
    {
        int a=n%10;
        b[a]=true;
        n/=10;
    }
}
bool check(bool *b)
{
    for(int i=0;i<10;i++)
    {
        if(!b[i])
            return false;
    }
    return true;
}
int main()
{
    ofstream out("out.txt");
    ifstream in("in.txt");
    int test;
    in>>test;
    for(int t=1;t<=test;t++)
    {
        long long int sum;
        long long int n;
        in>>n;
        bool b[10]={false};
        if(!n)
        {
            out<< "Case #"<<t<< ": "<< "INSOMNIA"<<endl;
            continue;
        }
        int i=1;
        while(1)
        {
            sum=n*(long long int)i;
            breaknfill(b,sum);
            if(check(b))
                break;
            i++;
        }
        out<< "Case #"<<t<< ": "<<sum<<endl;
    }
    return 0;
}
