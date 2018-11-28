#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int main()
{
ifstream in("A-large.in");
ofstream out("output.txt");
vector <unsigned long long> v ;
long test ;
in>>test;
long n , mut , temp , goal;

unsigned long long num , num1;
for(long i=0;i<10;i++)
{
    v.push_back(-1);
}
for(long j=1;j<=test ; j++)
{
    mut =1 ;
    in>>num;
    if(num==0)
        out <<"Case #"<<j <<": INSOMNIA"<<endl;
    else
    {
        for(long i=0;i<10;i++)
        {
            v[i]=-1;
        }

        n=0;

        while (n <10)
        {
            n=0;
            num1 = num * mut ;
            mut++;
            while(num1 != 0)
            {
                temp = num1 % 10;
                num1 = num1/10;
                v[temp] = 1;
            }

            for (long s=0; s<10 ;s++)
            {
                n+=v[s];
            }
        }
        mut--;
        out<<"Case #"<<j <<": "<< num*mut<<endl;

    }


}


return 0 ;
}
