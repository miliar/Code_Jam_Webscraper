#include <iostream>
#include <fstream>
using namespace std;

int finished(int num_c[])
{
    for(int i=0;i<10;i++)
        if(num_c[i]==0)
            return 0;
    return 1;
}

void update_num(int num_c[],int N,int i)
{
    int n=N*i,d;

    while(n!=0)
    {
        d=n%10;
        num_c[d]=1;
        n/=10;
    }
}

int main()
{
    ifstream input;
    input.open("A-large.in");
    ofstream output;
    output.open("out1.txt");

    int t;
    input>>t;

    for(int k=1;k<=t;k++)
    {
        int N;
        input>>N;
        //cout<<"T = "<<k<<" --- "<<N<<endl;
        int num_c[10];
        for(int i=0;i<10;i++)
            num_c[i]=0;

        int i;
        for(i=1;i<200;i++)
        {
            update_num(num_c,N,i);

            if( finished(num_c) )
            {
                output<<"Case #"<<k<<": "<<i*N<<endl;
                break;
            }
        }
        if(i>=200)
            output<<"Case #"<<k<<": INSOMNIA"<<endl;
    }
    //cout<<"DONE"<<endl;
    output.close();
    input.close();
    return 0;
}
