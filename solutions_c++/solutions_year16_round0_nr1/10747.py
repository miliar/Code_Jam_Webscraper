#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
        if(!fin)
        {
            cout<<"file cannot open correctly";
        }
    ofstream fout("output.in");

    long int N,num;
    int T,testcase=0,i,flag,rem,dig[10],j,tcount;
    testcase=0;
    fin>>T;
    while(testcase<T)
    {
        fin>>N;
        j=1;    flag=0;
        for(i=0;i<10;i++)
            dig[i]=-1;
        num=N;
        if(N==0)
        {
            fout<<"Case #"<<testcase+1<<": INSOMNIA"<<endl;
            testcase++;
        }
        else
        {
            while(flag==0)
            {
                tcount=0;
                while(num>0)
                {
                    rem=num%10;
                    dig[rem]=rem;
                    num/=10;
                }
                j++;
                num=j*N;
                for(i=0;i<10;i++)
                    if(dig[i]==-1)
                        tcount++;
                if(tcount>0)
                    flag=0;
                else
                    flag=1;
            }
            j--;
            fout<<"Case #"<<testcase+1<<": "<<j*N<<endl;
            testcase++;
        }
    }
}
