#include <iostream>
#include <fstream>
#include <set>
#include <math.h>

using namespace std;

long long isprime(long long number)
{
    for (long long i=2;i<sqrt(number);i++)
        if (number % i==0) {
            return i;
        }
    return 0;
}

long long convert(long long number,int base)
{
    if (base==10)
    {
        return number;
    }
    long long result=0;
    long long power=1;
    while (number>0)
    {
        result+=(number % 10) * power;
        number/=10;
        power*=base;
    }
    return result;
}

int main()
{
    int inputnumber,ii,n,N,J,countcopy;
    long long count;
    long long div;
    long long divs[11];
    int total=0;
    ifstream fin("input");
    ofstream fout("output");
    fin>>inputnumber;
    bool goodnumber;
    set<int> flag;
    for (int ii=1;ii<=inputnumber;ii++)
    {
        fout<<"Case #"<<ii<<":"<<endl;
        fin>>N>>J;
        total=0;
        for (long long countp=(1<<(N-1)); countp<(1<<N); countp++)
        {
            if (countp % 2==0)
                continue;
            countcopy=countp;
            count=0;
            long long power=1;
            while (countcopy>0)
            {
                count+=power*(countcopy % 2);
                countcopy/=2;
                power*=10;
            }
            cout<<count<<endl;
            goodnumber=true;
            for (int jj=2;jj<=10;jj++)
            {
                //cout<<"test:"<<convert(count,jj)<<endl;
                div=isprime(convert(count,jj));
                if (div==0)
                {
                    goodnumber=false;
                    break;
                }
                else
                {
                    divs[jj]=div;
                }
            }
            if (goodnumber)
            {
                total++;
                countcopy=count;
                string s="";
                while (countcopy>0)
                {
                    if (countcopy % 2==0)
                        s="0"+s;
                    else
                        s="1"+s;
                    countcopy/=2;
                }
                fout<<count;
                for (int i=2;i<=10;i++)
                    fout<<" "<<divs[i];
                fout<<endl;
                if (total==J)
                {
                    break;
                }
            }
        }
    }
    return 0;
}