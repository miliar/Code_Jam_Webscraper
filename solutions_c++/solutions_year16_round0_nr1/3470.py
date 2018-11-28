#include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("ouput.txt");

int main()
{
    long long  t;
    fin>>t;

    for(long long z=1;z<=t;z++)
    {
        long long n;
        fin>>n;
        long long x=0;
        long long temp=n;
        long long i=1;

        if(n==0)
            fout<<"Case #"<<z<<": INSOMNIA"<<endl;
        else
        {

            while(x!=1023)
            {
                i++;
                while(n>0)
                {
                    long long d=n%10;
                    x=x|(1<<d);
                    n=n/10;
                }
                n=temp*i;
            }

            fout<<"Case #"<<z<<": "<<(temp*(i-1))<<endl;
        }
    }
    return 0;
}
