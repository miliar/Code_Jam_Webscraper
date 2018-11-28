#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream coutt("output.txt");
    ifstream cinn("input.txt");
    int T;
    cinn>>T;
    for(int ii=0;ii<T;ii++)
    {
        int chk[10]={0,},chkn=0;
        coutt<<"Case #"<<ii+1<<": ";
        long long int nown;
        int n;

        cinn>>n;
        nown=n;
        if(n==0)
        {
            coutt<<"INSOMNIA"<<endl;
            continue;
        }
        for(;;)
        {
            int tmpn=nown;
            for(;;)
            {
                if(chk[tmpn%10]==0)
                {
                    chk[tmpn%10]=1;chkn++;
                }
                if(tmpn/10==0)break;
                tmpn/=10;
            }
            if(chkn==10)break;
            else nown+=n;
        }
        coutt<<nown<<endl;
    }
}
